import pandas as pd
import random
from datetime import datetime, timedelta

# Generate 30 days of data
start_date = datetime.today() - timedelta(days=29)

data = []

apps = {
    "Instagram": "Social Media",
    "YouTube": "Entertainment",
    "WhatsApp": "Social Media",
    "LinkedIn": "Social Media",
    "Netflix": "Entertainment",
    "Chrome": "Work",
    "Gmail": "Work"
}

for i in range(30):
    date = (start_date + timedelta(days=i)).date()
    
    for app, category in apps.items():
        usage_minutes = random.randint(10, 120)
        
        data.append([date, app, category, usage_minutes])

df = pd.DataFrame(data, columns=["date", "app_name", "category", "usage_minutes"])

df.to_csv("data/screen_time_data.csv", index=False)

print("Dataset Generated Successfully!")
