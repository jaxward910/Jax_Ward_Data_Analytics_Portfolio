#!/usr/bin/env python3
"""
Build a dataset for ALL NFL teams (2018–2024) containing, through Week 6 of each season:
- Wins
- Losses
- Point Differential (points_for - points_against, Weeks 1–6)
- Total Turnovers (INT thrown + fumbles lost, Weeks 1–6)
- Division Wins (wins vs. divisional opponents, Weeks 1–6)
- Total Offensive Yards (sum of yards gained on rush/pass plays by posteam, Weeks 1–6)
- Whether the team made the playoffs that season

DEPENDENCIES (install first):
    pip install nfl_data_py pandas pyarrow

NOTES:
- Uses nfl_data_py to pull schedules and play-by-play.
- Divisions are mapped via a static dictionary (NFL divisions have been stable since 2002).
- Offensive yards are computed from play-by-play: sum of 'yards_gained' where rush==1 or pass==1 for the posteam.
"""

import pandas as pd
from typing import List, Dict
import sys

try:
    import nfl_data_py as nfl
except Exception as e:
    sys.stderr.write("ERROR: nfl_data_py is required. Install with:\n  pip install nfl_data_py pandas pyarrow\n")
    raise

YEARS: List[int] = list(range(2015, 2026))   # 2018–2024 inclusive
OUT_CSV = "nfl_weeks1_6_2018_2024_with_divisions_offyards.csv"

# Static division map for nflfastR team abbreviations used 2018–2024
DIVISION_MAP: Dict[str, str] = {
    # AFC EAST
    "BUF":"AFC East","MIA":"AFC East","NE":"AFC East","NYJ":"AFC East",
    # AFC NORTH
    "BAL":"AFC North","CIN":"AFC North","CLE":"AFC North","PIT":"AFC North",
    # AFC SOUTH
    "HOU":"AFC South","IND":"AFC South","JAX":"AFC South","TEN":"AFC South",
    # AFC WEST (include OAK/LV for continuity)
    "DEN":"AFC West","KC":"AFC West","LAC":"AFC West","OAK":"AFC West","LV":"AFC West",
    # NFC EAST (WAS covers Football Team + Commanders)
    "DAL":"NFC East","NYG":"NFC East","PHI":"NFC East","WAS":"NFC East",
    # NFC NORTH
    "CHI":"NFC North","DET":"NFC North","GB":"NFC North","MIN":"NFC North",
    # NFC SOUTH
    "ATL":"NFC South","CAR":"NFC South","NO":"NFC South","TB":"NFC South",
    # NFC WEST (LA Rams are LAR; Cards are ARI)
    "ARI":"NFC West","LAR":"NFC West","SEA":"NFC West","SF":"NFC West",
}

def build_team_gameframe_from_schedules(sched: pd.DataFrame) -> pd.DataFrame:
    """Explode schedule rows into team-rows (home/away). Keep REG games, compute PF/PA and win flag per game."""
    reg = sched.loc[sched["game_type"] == "REG", ["season","week","game_id","home_team","away_team","home_score","away_score"]].copy()

    home = reg.rename(columns={
        "home_team":"team",
        "away_team":"opp",
        "home_score":"points_for",
        "away_score":"points_against"
    })
    home["is_win"] = (home["points_for"] > home["points_against"]).astype(int)

    away = reg.rename(columns={
        "away_team":"team",
        "home_team":"opp",
        "away_score":"points_for",
        "home_score":"points_against"
    })
    away["is_win"] = (away["points_for"] > away["points_against"]).astype(int)

    team_games = pd.concat([home[["season","week","game_id","team","opp","points_for","points_against","is_win"]],
                            away[["season","week","game_id","team","opp","points_for","points_against","is_win"]]],
                           ignore_index=True)
    return team_games

def compute_turnovers_from_pbp(pbp: pd.DataFrame) -> pd.DataFrame:
    """
    Compute giveaways per team per game from play-by-play:
      turnovers = interceptions thrown + fumbles lost
    Count when posteam is the possessing team and either interception==1 or fumble_lost==1.
    Return: [season, week, game_id, team, turnovers]
    """
    cols_needed = {"season","week","game_id","posteam","interception","fumble_lost","season_type"}
    missing = cols_needed - set(pbp.columns)
    if missing:
        raise ValueError(f"PBP is missing required columns for TOs: {missing}")

    pbp_reg = pbp.loc[pbp["season_type"] == "REG", ["season","week","game_id","posteam","interception","fumble_lost"]].copy()
    pbp_reg["interception"] = pbp_reg["interception"].fillna(0).astype(int)
    pbp_reg["fumble_lost"] = pbp_reg["fumble_lost"].fillna(0).astype(int)
    pbp_reg = pbp_reg[pbp_reg["posteam"].notna()].copy()

    pbp_reg["to_flag"] = pbp_reg["interception"] + pbp_reg["fumble_lost"]
    team_game_to = pbp_reg.groupby(["season","week","game_id","posteam"], as_index=False)["to_flag"].sum()
    team_game_to = team_game_to.rename(columns={"posteam":"team","to_flag":"turnovers"})
    return team_game_to

def compute_offensive_yards_from_pbp(pbp: pd.DataFrame) -> pd.DataFrame:
    """
    Compute total offensive yards per team per game from play-by-play.
    We sum 'yards_gained' on plays where posteam == team AND (rush==1 OR pass==1).
    This approximates net scrimmage yards (rush + pass, sacks & negative plays included).
    Return: [season, week, game_id, team, offensive_yards]
    """
    cols_needed = {"season","week","game_id","posteam","rush","pass","yards_gained","season_type"}
    missing = cols_needed - set(pbp.columns)
    if missing:
        raise ValueError(f"PBP is missing required columns for offensive yards: {missing}")

    pbp_reg = pbp.loc[pbp["season_type"] == "REG", ["season","week","game_id","posteam","rush","pass","yards_gained"]].copy()
    pbp_reg = pbp_reg[pbp_reg["posteam"].notna()].copy()

    pbp_reg["rush"] = pbp_reg["rush"].fillna(0).astype(int)
    pbp_reg["pass"] = pbp_reg["pass"].fillna(0).astype(int)
    pbp_reg["yards_gained"] = pbp_reg["yards_gained"].fillna(0).astype(int)

    scrimmage = pbp_reg[(pbp_reg["rush"]==1) | (pbp_reg["pass"]==1)].copy()
    team_game_oy = scrimmage.groupby(["season","week","game_id","posteam"], as_index=False)["yards_gained"].sum()
    team_game_oy = team_game_oy.rename(columns={"posteam":"team","yards_gained":"offensive_yards"})
    return team_game_oy

def tag_divisions(df: pd.DataFrame) -> pd.DataFrame:
    """Add division for 'team' and 'opp' using DIVISION_MAP."""
    df = df.copy()
    df["team_division"] = df["team"].map(DIVISION_MAP)
    df["opp_division"] = df["opp"].map(DIVISION_MAP)
    return df

def main():
    print("Loading schedules...")
    schedules = nfl.import_schedules(YEARS)

    # Build per-team game-level frame from schedules for REG only
    team_games = build_team_gameframe_from_schedules(schedules)

    # Add divisions for team and opponent
    team_games = tag_divisions(team_games)

    # Division games flag
    team_games["is_division_game"] = (team_games["team_division"].notna()) & (team_games["team_division"] == team_games["opp_division"])

    # Restrict to Weeks 1–6 for WL/PD and division wins
    tg_1_6 = team_games.loc[team_games["week"].between(1, 6)].copy()
    tg_1_6["point_diff"] = tg_1_6["points_for"] - tg_1_6["points_against"]
    tg_1_6["division_win"] = ((tg_1_6["is_division_game"]) & (tg_1_6["is_win"]==1)).astype(int)

    agg_wl_pd_div = (
        tg_1_6.groupby(["season","team"], as_index=False)
        .agg(
            Wins_Through_Week6 = ("is_win","sum"),
            Games = ("is_win","count"),
            Point_Differential_Wk1_6 = ("point_diff","sum"),
            Division_Wins_Wk1_6 = ("division_win","sum")
        )
    )
    agg_wl_pd_div["Losses_Through_Week6"] = agg_wl_pd_div["Games"] - agg_wl_pd_div["Wins_Through_Week6"]
    agg_wl_pd_div = agg_wl_pd_div.drop(columns=["Games"])

    # Compute turnovers and offensive yards from play-by-play
    print("Loading play-by-play (this can take a while)...")
    try:
        pbp = nfl.import_pbp_data(YEARS)
    except Exception:
        # Backcompat for older nfl_data_py versions
        pbp = nfl.import_pbp(YEARS)

    team_game_to = compute_turnovers_from_pbp(pbp)
    team_game_oy = compute_offensive_yards_from_pbp(pbp)

    # Merge turnovers and offensive yards onto team_games, then aggregate Weeks 1–6
    base_merge = team_games[["season","week","game_id","team"]].copy()

    team_to_1_6 = (
        base_merge.merge(team_game_to, on=["season","week","game_id","team"], how="left")
    )
    team_to_1_6["turnovers"] = team_to_1_6["turnovers"].fillna(0).astype(int)
    team_to_1_6 = team_to_1_6.loc[team_to_1_6["week"].between(1,6)]
    agg_to = (
        team_to_1_6.groupby(["season","team"], as_index=False)["turnovers"].sum()
        .rename(columns={"turnovers":"Total_Turnovers_Wk1_6"})
    )

    team_oy_1_6 = (
        base_merge.merge(team_game_oy, on=["season","week","game_id","team"], how="left")
    )
    team_oy_1_6["offensive_yards"] = team_oy_1_6["offensive_yards"].fillna(0).astype(int)
    team_oy_1_6 = team_oy_1_6.loc[team_oy_1_6["week"].between(1,6)]
    agg_oy = (
        team_oy_1_6.groupby(["season","team"], as_index=False)["offensive_yards"].sum()
        .rename(columns={"offensive_yards":"Total_Offensive_Yards_Wk1_6"})
    )

    # Playoff flag: any non-REG game appearance
    po = schedules.loc[schedules["game_type"] != "REG", ["season","home_team","away_team"]].copy()
    po_home = po.rename(columns={"home_team":"team"})[["season","team"]]
    po_away = po.rename(columns={"away_team":"team"})[["season","team"]]
    playoffs = pd.concat([po_home, po_away], ignore_index=True).dropna().drop_duplicates()
    playoffs["made_playoffs"] = "Y"

    # Combine all pieces
    result = (
        agg_wl_pd_div
        .merge(agg_to, on=["season","team"], how="left")
        .merge(agg_oy, on=["season","team"], how="left")
        .merge(playoffs, on=["season","team"], how="left")
    )
    result["made_playoffs"] = result["made_playoffs"].fillna("N")

    # Tidy columns
    result = result.rename(columns={
        "season":"Year",
        "team":"Team"
    })[
        ["Year","Team","Wins_Through_Week6","Losses_Through_Week6","Point_Differential_Wk1_6",
         "Total_Turnovers_Wk1_6","Division_Wins_Wk1_6","Total_Offensive_Yards_Wk1_6","made_playoffs"]
    ].sort_values(["Year","Team"])

    print(f"Writing CSV to {OUT_CSV} ...")
    result.to_csv(OUT_CSV, index=False)
    print("Done!")
    print(result.head(20))

if __name__ == "__main__":
    main()
