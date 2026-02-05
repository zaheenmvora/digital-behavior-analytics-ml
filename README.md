# 📊 Digital Behavior Analytics & Social Media Detox System

A Machine Learning-based digital behavior analysis system that evaluates screen-time patterns, detects potential addiction risk levels, and generates personalized detox recommendations.  
The project integrates data engineering, predictive modeling, clustering, and Power BI visualization to deliver actionable behavioral insights.

---

## 🚀 Project Overview

This project analyzes digital usage patterns to understand behavioral trends and potential overuse of social media.  
The system includes:

- Synthetic screen-time data generation
- Behavioral feature engineering
- Addiction risk score computation (0–100)
- Random Forest-based risk classification
- K-Means behavioral clustering
- Personalized detox recommendation engine
- Interactive Power BI dashboard visualization

This is a behavioral analytics prototype designed for research and educational purposes.

---

## 🧠 Analytical & ML Approach

The system follows an end-to-end data science pipeline:

### 1️⃣ Data Generation

- Generates 30 days of app usage data
- Includes:
  - Date
  - App Name
  - Category (Social Media / Work / Entertainment)
  - Usage Minutes

### 2️⃣ Feature Engineering

Derived behavioral metrics:

- Total daily usage hours
- Social media usage ratio
- Weekend vs weekday behavior
- Weekly social usage projection
- Target reduction estimation
- Monthly time saved estimation
- Normalized addiction risk score (0–100)

Risk Score Formula:

```
addiction_risk_score =
(total_hours × 10) + (social_media_ratio × 50)
```

Normalized across dataset for comparability.

---

## 🤖 Machine Learning Models

### 🔹 Classification Model

- Model: Random Forest Classifier
- Labels: Low / Medium / High Risk
- Train-Test Split: 80–20
- Features:
  - total_hours
  - social_media_ratio
  - weekly_social_hours

Outputs:

- Accuracy score
- Classification report
- Predicted risk levels

---

### 🔹 Clustering Model

- StandardScaler for feature normalization
- K-Means (n_clusters = 3)
- Behavioral segmentation into usage clusters

---

## 🎯 Recommendation Engine

A rule-based system generates personalized detox recommendations based on:

- Predicted addiction risk
- Social media dominance
- Behavioral patterns

Example outputs:

- "Enable app limits and avoid social media after 9 PM"
- "Reduce social media usage by 1 hour daily"
- "Maintain healthy digital habits"

---

## 📊 Power BI Dashboard

The Power BI dashboard visualizes:

- Daily & weekly usage trends
- Addiction risk distribution
- Behavioral clusters
- Predicted risk segmentation
- Detox impact projections
- Personalized recommendations

Screenshots are available in the `assets/` folder.

> Note: The Power BI (.pbix) file may not be previewable directly on GitHub.

---

## 📂 Project Structure

```
digital-behavior-analytics/
│
├── assets/
│   ├── dashboard_overview.png
│   ├── ml_insights.png
│   └── recommendations.png
│
├── data/
│   ├── screen_time_data.csv
│   ├── processed_detox_data.csv
│   ├── final_ml_output.csv
│   └── final_dashboard_data.csv
│
├── src/
│   ├── generate_data.py
│   ├── detox_engine.py
│   ├── ml_model.py
│   └── recommendation.py
│
├── notebooks/
│
├── social_media_detox_dashboard.pbix
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/digital-behavior-analytics.git
cd digital-behavior-analytics
```

Create virtual environment:

```bash
python -m venv venv
venv\Scripts\activate   # Windows
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## 🏋️ Running the Pipeline

### 1️⃣ Generate Dataset

```bash
python src/generate_data.py
```

### 2️⃣ Process Behavioral Data

```bash
python src/detox_engine.py
```

### 3️⃣ Train ML Models

```bash
python src/ml_model.py
```

### 4️⃣ Generate Recommendations

```bash
python src/recommendation.py
```

Final dashboard-ready dataset:

```
data/final_dashboard_data.csv
```

---

## 🛠 Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Random Forest
- K-Means Clustering
- StandardScaler
- Power BI

---

## ⚠️ Disclaimer

This system is designed for educational and behavioral analytics purposes only.  
It is not a medical or psychological diagnostic tool.

---

## 📜 License

MIT License

## Author

Zaheen M Vora

Computer Engineering Student | Aspiring Data Science and ML Engineer