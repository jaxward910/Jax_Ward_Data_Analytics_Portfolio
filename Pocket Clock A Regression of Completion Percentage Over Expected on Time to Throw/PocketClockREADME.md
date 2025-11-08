# 🕰️ Pocket Clock – Quarterback Efficiency Regression

**Author:** Jax Ward  
**Topic:** NFL Analytics | Quarterback Decision Efficiency | Sports Data Science  
**Tools:** R nflreadR nflfastR tidyverse broom nflplotR

---

## 🏈 Overview

This project explores how a quarterback’s **Time to Throw (TTT)** affects their **Completion Percentage Over Expected (CPOE)** — a modern efficiency metric widely used in football analytics.  
By applying **linear regression modeling**, the analysis identifies how decision speed correlates with accuracy beyond expectation and whether certain play-style archetypes outperform the model trend.

The project name, *Pocket Clock*, reflects how the timing of throws inside the pocket impacts expected performance outcomes.

---

## 🎯 Objectives

1. Quantify the statistical relationship between **CPOE** and **Time to Throw**.  
2. Identify quarterback groups who consistently **outperform or underperform** model expectations.  
3. Visualize regression trends to illustrate efficiency tradeoffs between fast vs. slow decision-making.  
4. Demonstrate predictive modeling workflow in a reproducible, football-specific context.

---

## 🧮 Methodology

- **Dataset:** Play-by-play or per-game quarterback stats (Time to Throw, CPOE, EPA/play, etc.).  
- **Preprocessing:** Data cleaned, filtered by qualified attempts, and standardized for comparability.  
- **Model:**  
  - Simple Linear Regression: `CPOE ~ Time_to_Throw`  

---

## 📊 Key Findings

- Moderate negative correlation between **time to throw** and **completion percentage over expected**, suggesting prolonged reads often reduce efficiency.  
- Certain quarterbacks (e.g., elite processors or mobile QBs) **outperform regression predictions**, showing context-dependent timing value.  
- Visualizations highlight clusters of quarterback styles — “quick-trigger passers” vs. “extended play creators.”

---

## 🧰 Technical Stack

| Category | Tools |
|-----------|-------|
| Language | R |
| Libraries | nflreadR nflfastR tidyverse broom nflplotR |
| Environment | Jupyter Notebook |
| Version Control | Git & GitHub |
| License | Apache 2.0 |

---

## 📈 Visualizations

- Scatterplots of CPOE vs. Time to Throw  


Example output:  
> “Quarterbacks maintaining sub-2.5s release times averaged +2.3% CPOE, outperforming model expectations by nearly one standard deviation.”

---

## 🚀 How to Run

1. Clone the repository  
   ```bash
   git clone https://github.com/jaxward910/Pocket_Clock.git
   cd Pocket_Clock
