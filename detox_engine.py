import pandas as pd

# Load Raw Data
df = pd.read_csv("data/screen_time_data.csv")

df["date"] = pd.to_datetime(df["date"])
df["usage_hours"] = df["usage_minutes"] / 60


# Daily Aggregation

daily = df.groupby("date").agg(
    total_hours=("usage_hours", "sum"),
    social_hours=("usage_hours", lambda x: x[df.loc[x.index, "category"] == "Social Media"].sum()),
    work_hours=("usage_hours", lambda x: x[df.loc[x.index, "category"] == "Work"].sum()),
    entertainment_hours=("usage_hours", lambda x: x[df.loc[x.index, "category"] == "Entertainment"].sum())
).reset_index()

# Fill missing category sums with 0
daily = daily.fillna(0)


# Social Media Ratio

daily["social_media_ratio"] = (
    daily["social_hours"] / daily["total_hours"]
).fillna(0)


# Weekend vs Weekday

daily["day_type"] = daily["date"].dt.day_name()
daily["is_weekend"] = daily["day_type"].isin(["Saturday", "Sunday"])


# Addiction Risk Score

daily["addiction_risk_score"] = (
    (daily["total_hours"] * 10) +
    (daily["social_media_ratio"] * 50)
)

# Normalize to 0–100
daily["addiction_risk_score"] = (
    100 * daily["addiction_risk_score"] / daily["addiction_risk_score"].max()
)

# Risk Level Category

def risk_level(score):
    if score >= 75:
        return "High"
    elif score >= 50:
        return "Moderate"
    else:
        return "Low"

daily["behavioral_risk_level"] = daily["addiction_risk_score"].apply(risk_level)

# Detox Plan Generator

def detox_recommendation(score):
    if score >= 75:
        return "Reduce by 30% using app timers and no-phone mornings."
    elif score >= 50:
        return "Reduce by 20% and avoid night scrolling."
    else:
        return "Maintain current usage and track weekly."

daily["detox_recommendation"] = daily["addiction_risk_score"].apply(detox_recommendation)

# Weekly & Monthly Insights

daily["weekly_social_hours"] = daily["social_hours"] * 7
daily["target_reduction_hours"] = daily["weekly_social_hours"] * 0.3
daily["monthly_time_saved"] = daily["target_reduction_hours"] * 4

# Save Processed File

daily.to_csv("data/processed_detox_data.csv", index=False)

print("Detox Data Processed Successfully.")
