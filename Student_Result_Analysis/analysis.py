import pandas as pd

# Read CSV file
data = pd.read_csv(r"C:\Users\Lenovo\OneDrive\Desktop\Student_result_analysis\student_data.csv")

# Display data
print("Student Data:")
print(data)

# Calculate average marks
data["Average"] = (
    data["Maths"] +
    data["Science"] +
    data["English"]
) / 3

print("\nAverage Marks:")
print(data[["Name", "Average"]])

# Find topper
topper = data.loc[data["Average"].idxmax()]

print("\nTopper:")
print(topper["Name"])
print("Average Marks:", topper["Average"])

import matplotlib.pyplot as plt

plt.bar(data["Name"], data["Average"])

plt.title("Student Average Marks")
plt.xlabel("Students")
plt.ylabel("Average Marks")

plt.show()