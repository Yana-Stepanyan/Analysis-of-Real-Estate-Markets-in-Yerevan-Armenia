#  Analysis of Real Estate Markets in Yerevan, Armenia

This project analyzes **real estate data in Yerevan** by scraping public listings, cleaning and preparing the dataset, performing exploratory analysis, and building a **predictive model for apartment prices** using machine learning.

The goal is to **understand the factors influencing property prices in Yerevan** and to develop a reproducible pipeline for price prediction and market analysis.

---

##  Project Structure

```   
Analysis-of-Real-Estate-Markets-of-Armenia
│
├── data/                  # Cleaned and raw datasets
├── notebooks/             # Jupyter notebooks for EDA and modeling
├── src/                   # Scripts for Scraping
│
├── Requirements.txt       # Project dependencies
└── README.md              # Project documentation
```

---

## 🗂 Dataset

The dataset was **scraped from publicly available Armenian real estate listing websites**, focusing on Yerevan apartments.

### Final cleaned dataset shape:

* **Rows:** 4003
* **Columns:** 7 (`District`, `Building Type`, `Rooms`, `Area`, `Floor`, `Renovation`, `Price`)

### Key preprocessing steps:

✅ Removed rare/irrelevant categories

✅ Filtered out non-Yerevan data

✅ Removed outliers using IQR while retaining market distribution

✅ Standardized data types and cleaned numeric columns

---

##  Exploratory Data Analysis (EDA)

EDA was performed to:

* Understand the distribution of **area and price**.
* Identify the most common districts and room counts.
* Explore the relationship between `Area`, `Rooms`, and `Price`.
* Visualize outlier removal and its effect on distributions.

---

##  Modeling

A **regression model** was built to predict apartment prices in Yerevan using the cleaned dataset.

### Evaluation Metrics

* **Mean Absolute Error (MAE):** \~\$16,000 USD
* **Root Mean Squared Error (RMSE):** \~\$24,000 USD
* **R² Score:** \~0.77

These results indicate **strong predictive accuracy**, with consistent performance across hold-out evaluation and cross-validation.

These results are **strong for this dataset and market**, demonstrating that the model can **capture meaningful patterns in Yerevan’s real estate prices while maintaining practical prediction accuracy for informed decision-making.**

---


## Results and Insights

✅ Developed a **clean, analysis-ready Yerevan real estate dataset**.

✅ Identified **key drivers of price** (Area, Rooms, District).

✅ Built a **practical predictive model** for price estimation.

✅ Created **reusable scraping, cleaning, and modeling workflows**.

---
## ️ Setup Instructions

1️⃣ Clone the repository:

```bash
git clone https://github.com/Yana-Stepanyan/Analysis-of-Real-Estate-Markets-of-Armenia.git
cd Analysis-of-Real-Estate-Markets-of-Armenia
```

2️⃣ Install dependencies:

```bash
pip install -r Requirements.txt
```

3️⃣ Run the scraping or analysis notebooks/scripts as needed.

---

## Why This Project Matters

✅ Demonstrates **real-world data collection, cleaning, and modeling** on a **locally relevant problem**.

✅ Supports **data-driven decision-making** for the Armenian real estate market.

✅ Serves as a **practical Data Science pipeline** for learning and portfolio showcasing.

---
