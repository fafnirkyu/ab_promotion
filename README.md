# 📊 A/B Testing: Fast-Food Promotion Campaign Analysis

## Overview
This project analyzes a controlled experiment run by a fast-food chain testing **three marketing campaigns** for a new menu item. Using A/B testing methodology, we identify which promotion generates the highest sales uplift.

## Dataset
- Weekly sales for 4 weeks across multiple markets.
- Covariates: Market size, store age, and location.
- [Dataset source](https://www.kaggle.com/datasets/chebotinaa/fast-food-marketing-campaign-ab-test/data).

## Tools
- Python (pandas, numpy, statsmodels, scipy, matplotlib, seaborn, scikit-posthocs)
- Bootstrapping methods for robust inference
- ANOVA, regression adjustment, power analysis

## Key Results
- **Promotion 2 significantly outperformed both Promotion 1 and Promotion 3.**
- Uplift: ~25% increase in sales over Promotion 1.
- Recommendation: Roll out Promotion 2 chain-wide.

## Deliverables
- 📓 [Analysis Notebook](notebook/analysis.ipynb)  
- 📑 [Executive Summary](reports/summary.pdf)

## Resume Bullet
“Performed A/B test analysis on fast-food marketing campaigns (design checks, ANOVA, regression adjustment, bootstrapped confidence intervals) and delivered actionable business recommendation.”
