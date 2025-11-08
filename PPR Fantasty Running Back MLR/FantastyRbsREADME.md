# 🏈 Fantasy Running Back Performance – Multiple Linear Regression (MLR)

**Author:** Jax Ward  
**Topic:** Fantasy Football Analytics | Predictive Modeling | Data Science in Sports  
**Tools:** R, tidyverse, nflverse, broom, car, kableextra  

---

## 📘 Overview

This project builds a **Multiple Linear Regression (MLR)** model to predict **fantasy football running back performance** using player-level statistics such as carries, targets, and touchdowns.  
The goal is to identify which variables most strongly explain week-to-week fantasy point totals — offering both predictive insight and strategic decision-making support for fantasy managers and analysts.

---

## 🎯 Objectives

1. Develop a statistical model predicting ppr running back fantasy points per game.  
2. Quantify the influence of volume, efficiency, and usage metrics on player performance.  
3. Detect multicollinearity between predictors (e.g., carries vs. touches).  
4. Translate results into actionable fantasy takeaways.

---

## 🧮 Methodology

- **Data Source:** Player-level fantasy data (seasonal or weekly) including rushing and receiving stats.  
- **Dependent Variable:** Fantasy Points (PPR format).  
- **Independent Variables:**  
  - `rush_attempts`  
  - `rush_yards`  
  - `receptions`  
  - `rec_yards`  
  - `rushing_tds`  
  - `recieving_tds`  
  - `snap_share`   
- **Model Used:** Multiple Linear Regression  
  - `Fantasy_Points ~ Rush_Attempts + targets + Total_TDs + snap_count`  
- **Diagnostics:**  
  - Variance Inflation Factor (VIF) to check multicollinearity  
  - Residual analysis for model fit  
  - Adjusted R² for model strength  

---

## 📊 Key Insights

- **Touch volume** and **touchdown rate** are the two most statistically significant predictors of fantasy production.  
- **Efficiency stats** (like yards per touch) add marginal predictive power but primarily help identify breakout candidates.  
- **Receiving usage** drives upside in PPR scoring formats.  
- Model R² ≈ **0.87**, showing a strong explanatory fit for the chosen variables.  

---

## ⚙️ Technical Stack

| Category | Tools / Packages |
|-----------|------------------|
| Programming | R |
| Libraries | tidyverse, nflverse, broom, car, kableextra   |
| Analysis | Multiple Linear Regression, Multicollinearity Testing |
| Visualization | Barcharts, Coefficient Plots, Residual tables |
| Environment | Jupyter Notebook |
| License | Apache 2.0 |

---


## 🚀 How to Run

1. Clone the repository  
   ```bash
   git clone https://github.com/jaxward910/Fantasy_RB_MLR.git
   cd Fantasy_RB_MLR
