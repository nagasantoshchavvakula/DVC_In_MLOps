import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib

# Read CSV with correct encoding
data = pd.read_csv('Linear_Regression_Data.csv', encoding='utf-16')


# Print columns to debug
print("Columns found:", data.columns.tolist())

# Strip whitespace from column names
data.columns = data.columns.str.strip()

# Optional: Fix hidden BOM character if present
if 'ï»¿YearsExperience' in data.columns:
    data.rename(columns={'ï»¿YearsExperience': 'YearsExperience'}, inplace=True)

# Check again
print("Cleaned columns:", data.columns.tolist())

# Define features and target
x = data[['YearsExperience']]
y = data['Salary']

# Train model
model = LinearRegression()
model.fit(x, y)

# Save model
joblib.dump(model, 'model.pkl')
print("Model trained and saved successfully.")
