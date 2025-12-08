# **MLB Hitter Archetypes: PCA and Clustering Analysis**

A data driven exploration of MLB hitter performance using advanced analytics, dimensionality reduction, and clustering.

---

## **Project Overview**

This project analyzes multi season MLB hitter data to uncover the underlying structure of offensive performance. Using Exploratory Data Analysis (EDA), Principal Component Analysis (PCA), and K means clustering, the project identifies meaningful hitter archetypes based on power, contact quality, plate discipline, speed, situational value, and batted ball tendencies.

The goal is to classify hitters by how they create value rather than relying only on traditional box score numbers.

---

## **Objectives**

- Identify key performance patterns through EDA  
- Reduce high dimensional hitter data using PCA  
- Cluster batters into interpretable offensive profiles  
- Visualize and compare clusters using radar charts and normalized bar charts  
- Provide insights that support scouting, player development, and analytical modeling  

---

## **Data Description**

The dataset includes a comprehensive collection of hitting metrics across several MLB seasons.

### **Traditional Stats**
G, PA, AB, H, 1B, 2B, 3B, HR  
R, RBI, BB, IBB, SO, HBP  
SB, CS, AVG  

### **Batted Ball Metrics**
GB, FB, LD, IFFB  
GB_pct, FB_pct, LD_pct, GB_FB  
HR_FB  
Barrel_pct, HardHit_pct  
Exit Velocity (EV)  
IFH, BU, BUH and their percentages  

### **Plate Discipline**
BB_pct, K_pct, BB/K  
Pitches, Balls, Strikes  

### **Run Value and Quality Metrics**
wOBA, wRAA, wRC, wRC_plus  
WAR, RAR, Dollars  
Offense, Defense, Batting, Replacement  
WPA, WPA_minus, WPA_plus  
RE24, REW  
pLI, Clutch  

### **Baserunning and Positional Metrics**
Spd, BaseRunning, wBsR  
Positional value adjustments  

These features collectively describe a hitter’s approach, quality of contact, run creation ability, and overall baseball value.

---

## **Methodology**

### **1. Exploratory Data Analysis (EDA)**

Initial visualizations explore foundational relationships, including:

- OPS vs Handedness  
- wOBA vs Exit Velocity  
- Home Runs vs Barrel Percentage  
- Distribution of Exit Velocity  

These confirm well known trends: contact quality drives performance, and simplistic traits like handedness do not explain much variance.

---

### **2. Principal Component Analysis (PCA)**

PCA reduces the large set of correlated features into orthogonal components that represent core skill dimensions.

#### **Key Components**

- **PC1** Overall production and power output  
- **PC2** Discipline and approach  
- **PC3** Speed and baserunning versus power  
- **PC4–PC5** Line drive contact, BABIP skill, situational value  

The first 8 components explain roughly **76 percent** of total variance, preserving primary hitter tendencies while filtering noise.

---

### **3. K Means Clustering**

K means clustering is applied to the PCA transformed data to identify groups of hitters with similar offensive profiles.

Cluster visualizations include:

- Radar charts summarizing each cluster's normalized trait profile  
- Bar charts comparing variables across clusters  

These clusters represent archetypes such as:

- Power driven sluggers  
- High contact groundball hitters  
- Balanced everyday players  
- Speed and contact specialists  
- Lower impact or developing hitters  

---

## **Key Insights**

- Contact quality (EV, Barrel_pct) is one of the strongest predictors of offensive value.  
- OPS does not differ significantly by hitter handedness.  
- Barrel_pct strongly correlates with home run output.  
- PCA reveals interpretable axes of variation for hitter evaluation.  
- Clustering identifies meaningful player types for scouting and analysis.  

---

## **Conclusion**

This project demonstrates that hitter performance is multi dimensional and best understood through statistical decomposition and clustering. By integrating EDA, PCA, and K means, the analysis provides a structured, data backed framework for comparing offensive profiles across MLB hitters.

---
