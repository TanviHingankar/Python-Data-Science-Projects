import pandas as pd
import os

from sklearn.tree import DecisionTreeClassifier

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

csv_path = os.path.join(BASE_DIR, "customer_churn.csv")

data = pd.read_csv(csv_path)

print("Dataset:")
print(data)

# Features
X = data[["Age", "MonthlyCharges", "Tenure"]]

# Target
y = data["Churn"]

# Create Model
model = DecisionTreeClassifier()

# Train Model
model.fit(X, y)
from sklearn.metrics import accuracy_score

y_pred = model.predict(X)

accuracy = accuracy_score(y, y_pred)

print("\nModel Accuracy:")
print(f"{accuracy * 100:.2f}%")

print("\nModel trained successfully!")

# User Input
age = int(input("Enter Age: "))
charges = float(input("Enter Monthly Charges: "))
tenure = int(input("Enter Tenure (Months): "))

new_customer = pd.DataFrame(
    [[age, charges, tenure]],
    columns=["Age", "MonthlyCharges", "Tenure"]
)

prediction = model.predict(new_customer)

if prediction[0] == 1:
    print("\nCustomer likely to leave (Churn)")
else:
    print("\nCustomer likely to stay")


