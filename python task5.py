import pandas as pd

january = pd.DataFrame({
    "order_id": ["J1", "J2", "J3"],
    "customer_id": [101, 102, 101],
    "amount": [500, 600, 700]
})

february = pd.DataFrame({
    "order_id": ["F1", "F2", "F3"],
    "customer_id": [103, 101, 102],
    "amount": [300, 800, 400]
})

combined = pd.concat(
    [january, february],
    ignore_index=True
)

print("Combined monthly orders:")
print(combined)

result = combined.groupby("customer_id").agg(
    total=("amount", "sum"),
    orders=("order_id", "count")
)

print("Customer summary:")
print(result)