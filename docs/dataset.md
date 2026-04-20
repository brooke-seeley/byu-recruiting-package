---
title: "Dataset Construction"
nav_order: 4
has_children: true
---

This project uses a custom-built dataset of football recruits to model the probability of committing to BYU. Since no single source contained all necessary information, I assembled the dataset by combining multiple scraping and feature engineering steps.

The full process can be understood in three stages:

---

## Overview of the Pipeline

1. **Scrape Top 247 Players**  
   Collect nationally ranked players and their attributes (height, weight, composite score)

2. **Scrape Non-Top Players**  
   Identify and extract the same data as above for additional players not included in the top 247 lists

3. **Calculate Distance Feature**  
   Compute the distance between each player’s previous school and BYU

---

## Step-by-Step Walkthrough

The following pages document how I did each step in detail:

### 1. Top 247 Players  
Scraping the main ranking lists and building the foundation of the dataset  
- [Top 247 Scraping](./notebooks/top_pages.md)

---

### 2. Non-Top Players  
Extending the dataset by identifying players outside the top rankings using position-based scraping  
- [Non-Top Player Scraping](./notebooks/non_top_pages.md)

---

### 3. Distance Feature Engineering  
Calculating geographic distance using latitude and longitude coordinates  
- [Distance Calculation](./notebooks/distance_calc.md)

---

## Final Dataset

The outputs from these steps were combined into a single dataset used for modeling. Key features include:

- Player attributes (height, weight, score)
- Recruiting rank indicator (`247Top`)
- Distance to BYU
- Additional demographic and contextual variables