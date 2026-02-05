import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report, accuracy_score

# Load processed data
df = pd.read_csv("data/processed_detox_data.csv")

# Create labels
def label_risk(score):
    if score < 40:
        return "Low"
    elif score < 70:
        return "Medium"
    else:
        return "High"

df["addiction_label"] = df["addiction_risk_score"].apply(label_risk)

# Features
features = [
    "total_hours",
    "social_media_ratio",
    "weekly_social_hours"
]

X = df[features]
y = df["addiction_label"]

# Train model
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Save predictions
df["predicted_risk"] = model.predict(X)

# CLUSTERING
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

kmeans = KMeans(n_clusters=3, random_state=42)
df["behavior_cluster"] = kmeans.fit_predict(X_scaled)

# Save output
df.to_csv("data/final_ml_output.csv", index=False)

print("ML models completed successfully")


y_pred_test = model.predict(X_test)

print("Accuracy:", accuracy_score(y_test, y_pred_test))
print(classification_report(y_test, y_pred_test))
