import pandas as pd
import numpy as np
from datetime import datetime, timedelta

np.random.seed(42)

n_rows = 10000

start_date = datetime(2024, 1, 1)
dates = [start_date + timedelta(days=np.random.randint(0, 365)) for _ in range(n_rows)]

departments = ["Payments", "Operations", "Compliance", "Settlements"]

data = {
    "transaction_id": range(1, n_rows + 1),
    "order_date": dates,
    "department": np.random.choice(departments, n_rows),
    "processing_time_minutes": np.random.gamma(shape=2, scale=15, size=n_rows).astype(int),
    "amount": np.round(np.random.uniform(100, 10000, n_rows), 2)
}

df = pd.DataFrame(data)

df["status"] = np.where(df["processing_time_minutes"] > 60, "Delayed", "Completed")
df["error_flag"] = np.where(df["processing_time_minutes"] > 90, 1, 0)

df.to_csv("data/raw/transactions_raw.csv", index=False)

print("Raw dataset generated:", df.shape)
