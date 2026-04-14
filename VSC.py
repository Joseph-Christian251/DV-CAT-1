import pandas as pd

data = {
    "Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
    "PassengerCount": [112, 118, 132, 129, 121, 135],
    "AvgTemp": [23, 24, 26, 27, 28, 30],
    "Rainfall": [12, 8, 10, 9, 15, 11]
}

df = pd.DataFrame(data)

# Variance
variance = df["PassengerCount"].var()

# Standard deviation
std_dev = df["PassengerCount"].std()

# Correlation (only numeric columns)
correlation = df.select_dtypes(include=[float, int]).corr()

print("Variance:", variance)
print("Standard Deviation:", std_dev)
print("Correlation:\n", correlation)

print(df)