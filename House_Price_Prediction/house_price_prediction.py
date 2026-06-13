import pandas as pd
import os

from sklearn.linear_model import LinearRegression

# Get current folder
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Read dataset
csv_path = os.path.join(BASE_DIR, "house_price.csv")

data = pd.read_csv(csv_path)

print("Dataset:")
print(data)

# Input feature (Area)
X = data[["Area"]]

# Output target (Price)
y = data["Price"]

# Create model
model = LinearRegression()

# Train model
model.fit(X, y)

print("\nModel trained successfully!")

# Prediction
# User Input
area = float(input("Enter house area in sq.ft: "))

predicted_price = model.predict(
    pd.DataFrame([[area]], columns=["Area"])
)

print("\nPredicted House Price:")
print(f"₹ {predicted_price[0]:,.2f}")

import matplotlib.pyplot as plt

# Actual data points
plt.scatter(data["Area"], data["Price"], label="Actual Data")

# Regression line
plt.plot(data["Area"], model.predict(X), label="Regression Line")

plt.title("House Price Prediction")
plt.xlabel("Area (sq.ft)")
plt.ylabel("Price")
plt.legend()

plt.show()

from sklearn.metrics import r2_score

y_pred = model.predict(X)

score = r2_score(y, y_pred)

print("\nModel Accuracy (R² Score):")
print(score)