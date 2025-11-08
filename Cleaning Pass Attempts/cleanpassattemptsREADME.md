# 🏈 PFR-Style QB Pass Attempt Counter

**Author:** Jax Ward  
**Topic:** NFL Data Engineering | Sports Analytics | Data Cleaning Logic  
**Tools:** Python, pandas, regex, nfl_data_py, statsmodels  

---

## 📘 Overview

This project builds a **customized pass attempt counter** that replicates how official stat providers (like **Pro Football Reference** or **ESPN**) define *quarterback pass attempts* — rather than relying blindly on raw play-by-play flags.  

Because public NFL datasets often miscount attempts due to penalties, spikes, sacks, or nullified plays, this logic enforces a **rule-based filtering system** to return *accurate, contextually valid* QB attempts per game, week, or season.

It’s built to sit atop **nfl_data_py**, the open-source play-by-play library, and ensures that all excluded or counted plays align with official NFL statistical definitions.

---

## 🎯 Objectives

1. Accurately count a quarterback’s official **pass attempts** for any given season, week, team, and player.  
2. Remove “manufactured” incomplete passes caused by defensive fouls (e.g., DPI).  
3. Exclude nullified or special-case plays such as two-point attempts, offsetting penalties, or “no play” outcomes.  
4. Provide an optional detailed output (`return_details=True`) to inspect which plays were included or excluded.

---

## 🧮 Methodology

- **Base Data:** Play-by-play data imported using `nfl_data_py.import_pbp_data()` across multiple seasons.  
- **Logic Foundation:**  
  - Excludes `two_point_attempt`, `offsetting penalties`, `no play` outcomes.  
  - Drops accepted *defensive* penalties (DPI, Illegal Contact, Defensive Holding) only when they **create an incompletion**.  
  - Includes accepted penalties otherwise — consistent with official scoring rules.  
  - Combines `qb_throwaway` and `throwaway` columns for consistency.  
  - Counts only plays where the QB is correctly attributed as the passer or spiker.  
- **Final Output:**  
  - The count of valid pass attempts.  
  - Optionally, a detailed DataFrame of qualifying plays for debugging and transparency.

---

## ⚙️ Core Functions

### `count_qb_pass_attempts_pfr(df, season, week, qb_name, team, return_details=False)`
Computes official QB pass attempts per game/week, with logic replicating ESPN/PFR standards.

**Parameters:**
- `df`: Play-by-play DataFrame from `nfl_data_py`
- `season`: Year of season (e.g., 2022)
- `week`: NFL week number
- `qb_name`: Quarterback short name format (e.g., `"J.Allen"`)
- `team`: Team abbreviation (e.g., `"BUF"`)
- `return_details`: If `True`, returns both the count and a detailed DataFrame of qualifying plays

**Returns:**  
- Integer (count of official pass attempts)  
- Optional DataFrame (when `return_details=True`)

---

### `debug_mismatch(df, season, week, qb_name, team)`
Helper function that returns both the counted plays and all plays from that week, allowing easy inspection of exclusions.

---

## 🧰 Technical Stack

| Category | Tools / Libraries |
|-----------|-------------------|
| Language | Python |
| Data Handling | pandas, numpy |
| Text Processing | re (regular expressions) |
| Sports Data Source | nfl_data_py |
| Modeling Support (optional) | statsmodels, scipy |
| Visualization | matplotlib, seaborn |

---

## 🧠 Example Usage

```python
import nfl_data_py as nfl
seasons = range(2016, 2022 + 1)
pbp_py = nfl.import_pbp_data(seasons)

# Compute official QB attempts
print("Brees 2016 Wk1:", count_qb_pass_attempts_pfr(pbp_py, 2016, 1, "D.Brees", "NO"))
print("Allen 2022 Wk1:", count_qb_pass_attempts_pfr(pbp_py, 2022, 1, "J.Allen", "BUF"))

# Expected output:
# Brees 2016 Wk1: 42
# Allen 2022 Wk1: 31
