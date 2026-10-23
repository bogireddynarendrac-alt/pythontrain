import pandas as pd

orders = pd.DataFrame({
    "order_id": ["1", "2", "3", "4", "5"],
    "customer_id": [101, 102, 101, 103, 104],
    "amount": [500, 600, 700, 300, 900]
})

customers = pd.DataFrame({
    "customer_id": [101, 102, 103, 105],
    "name": ["Arun", "Priya", "Rahul", "Divya"],
    "city": ["Chennai", "Mumbai", "Chennai", "Bangalore"]
})

customers.to_csv("customers.csv", index=False)

inner = pd.merge(
    orders, customers,
    on="customer_id",
    how="inner"
)

print("Inner join:")
print(inner)
print("Inner join rows:", len(inner))

left = pd.merge(
    customers, orders,
    on="customer_id",
    how="left",
    indicator=True
)

no_orders = left[left["_merge"] == "left_only"]
print("Customers with no orders:")
print(no_orders["name"].tolist())

outer = pd.merge(
    orders, customers,
    on="customer_id",
    how="outer",
    indicator=True
)

unmatched = outer[outer["_merge"] == "left_only"]

print("Orders without customer records:")
print(unmatched[["order_id", "customer_id", "amount"]])

print("Inner join: Returns only matching records.")
print("Left join: Returns all left-side records and matching right-side records.")
print("Outer join: Returns all records from both datasets.")