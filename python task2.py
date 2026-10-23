import pandas as pd

data = {
    "id": [1, 2, 3, 4, 5, 6, 7, 8],
    "name": [
        "Arun", "Priya", "Rahul", "Divya",
        "Karthik", "Meena", "Suresh", "Anitha"
    ],
    "department": [
        "Sales", "HR", "IT", "IT",
        "Finance", "Sales", "IT", "HR"
    ],
    "salary": [
        30000, 45000, 60000, 75000,
        90000, 52000, 68000, 48000
    ],
    "city": [
        "Chennai", "Chennai", "Bangalore", "Chennai",
        "Mumbai", "Bangalore", "Chennai", "Mumbai"
    ]
}

df = pd.DataFrame(data)
df.to_csv("employees.csv", index=False)

df = pd.read_csv("employees.csv")

print("First five rows:")
print(df.head())

print("DataFrame information:")
df.info()

print("Statistical summary:")
print(df.describe())

print("Name column:")
print(df["name"])

print("Name and salary columns:")
print(df[["name", "salary"]])

chennai = df.loc[df["city"] == "Chennai", "name"]
print("Chennai employees:", chennai.tolist())

print("Using iloc:")
print(df.iloc[0:3, 1:3])

high_salary = df[df["salary"] > 50000]
print("Employees earning above 50000:")
print(high_salary)
print("Count:", len(high_salary))

it_employees = df[df["department"] == "IT"]
print("IT employees:", it_employees["name"].tolist())
print("Count:", len(it_employees))