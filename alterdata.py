import pandas as pd

data = pd.read_csv('Linear_Regression_Data.csv',encoding='utf-8', sep=',')

data.columns = data.columns.str.strip()

# print(data.head())

data['YearsExperience'] = 2*data['YearsExperience']

data.to_csv('Linear_Regression_Data.csv', index=False)
print("Data updated successfully.")