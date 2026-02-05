import pandas as pd

df = pd.read_csv("data/final_ml_output.csv")

def recommend(row):
    if row["predicted_risk"] == "High":
        return "Enable app limits and avoid social media after 9 PM"
    elif row["social_media_ratio"] > 0.5:
        return "Reduce social media usage by 1 hour daily"
    else:
        return "Maintain healthy digital habits"

df["detox_recommendation"] = df.apply(recommend, axis=1)

df.to_csv("data/final_dashboard_data.csv", index=False)

print("Recommendations generated")
