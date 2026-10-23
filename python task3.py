import pandas as pd

data = {
    "order_id": [1, 2, 3, 3, 4, 5],
    "customer_id": [101, 102, 101, 101, 103, 104],
    "amount": [500, None, 700, 700, 300, 900]
}

df = pd.DataFrame(data)
df.to_csv("orders.csv", index=False)

df = pd.read_csv("orders.csv")

print("Missing values:")
print(df.isna().sum())

print("Duplicate rows:")
print(df.duplicated())
print("Duplicate count:", df.duplicated().sum())

df = df.drop_duplicates()

df["amount"] = pd.to_numeric(df["amount"])
median_amount = df["amount"].median()

print("Median used:", median_amount)

df["amount"] = df["amount"].fillna(median_amount)
df["order_id"] = df["order_id"].astype(str)

print("Cleaned data:")
print(df)

result = df.groupby("customer_id").agg(
    total=("amount", "sum"),
    orders=("order_id", "count")
)

print("Customer summary:")
print(result)