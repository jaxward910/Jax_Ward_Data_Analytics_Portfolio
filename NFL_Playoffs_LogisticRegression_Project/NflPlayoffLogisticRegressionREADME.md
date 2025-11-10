# 🏆 NFL Playoffs Prediction – Logistic Regression Model

**Author:** Jax Ward  
**Topic:** Sports Analytics | Predictive Modeling | NFL Data Science  
**Tools:** Python, pandas, scikit-learn, statsmodels, matplotlib, seaborn, os  

---

## 📘 Overview

This project uses **Logistic Regression** to model the probability of an NFL team making the playoffs based on early-season performance metrics.  
By analyzing team-level data such as wins, divisional wins, point differential, and offensiveyards, and total turnovers the model estimates **P(playoffs = 1)** for each team and evaluates predictive performance using key classification metrics.

The project demonstrates how data-driven modeling can transform raw stats into meaningful probabilities for sports strategy, betting, and fan engagement.

---

## 🎯 Objectives

1. Predict whether an NFL team will make the playoffs based on regular-season statistics.  
2. Evaluate model accuracy using confusion matrices, ROC curves, and AUC scores.  
3. Interpret coefficients to understand which factors most strongly influence playoff qualification.  
4. Apply classification metrics to measure precision, recall, and overall model reliability.

---

## 🧮 Methodology

- **Dataset:** Historical NFL team data (e.g., 2015–2024 seasons).  
- **Dependent Variable:** `Playoffs` (binary: 1 = made playoffs, 0 = missed).  
- **Independent Variables:**  
  - `Wins_Through_Week6`  
  - `divisional wins`  
  - `losses`  
  - `Total Turnovers`  
  - ` Team Offensive Yards`  

- **Model:** Logistic Regression (`Logit` from `statsmodels`)  
  - `Playoffs ~ Wins_Through_Week6 + Losses + division wins + Point_Differential + Turnovers + Total Offensive Yards`  
- **Performance Metrics:**  
  - Accuracy, Precision, Recall  
  - ROC Curve & AUC  
  - Confusion Matrix Visualization  

---

## 📊 Key Insights

- **Early-season wins** are the single strongest predictor of playoff qualification.  
- **Turnover differential** and **point differential** significantly improve predictive accuracy.  
- Model AUC ≈ **0.84**, showing strong separation between playoff and non-playoff teams.  
- Logistic coefficients reveal marginal gains in playoff odds per win or point differential increase.


---

## ⚙️ Technical Stack

| Category | Tools / Libraries |
|-----------|-------------------|
| Language | Python |
| Libraries | pandas, numpy, scikit-learn, statsmodels, matplotlib, seaborn, os |
| Modeling | Logistic Regression |
| Evaluation | ROC/AUC, Confusion Matrix, Precision-Recall |
| Environment | Jupyter Notebook |
| License | Apache 2.0 |

---

## 📈 Visualizations

- **ROC Curve:** Demonstrates model discrimination ability (AUC).  
- **Confusion Matrix:** Highlights classification performance.  
- **Feature Coefficient Chart:** Shows relative predictor importance.  
- **Probability Distribution Plot:** Compares predicted playoff odds by division or team.

---

## 🚀 How to Run

1. Clone the repository  
   ```bash
   git clone https://github.com/jaxward910/NFL_Playoffs_Logistic_Regression.git
   cd NFL_Playoffs_Logistic_Regression
