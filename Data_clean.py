import pandas as pd
import numpy as np
data = {
    'name': ['Alice', 'Bob', 'Charlie', np.nan, 'Eve'],
    'age': [24, np.nan, 22, 23, np.nan],
    'city': ['New York', 'Los Angeles', 'Chicago', np.nan, 'Houston'],
}
df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)
print("\nMissing values in each column:")
print(df.isnull().sum())
print("\nPercentage of missing values in each column:")
print(df.isnull().mean() * 100)
df_dropped = df.dropna()
print("\nDataFrame after dropping rows with missing values:")
print(df_dropped)
df['age'].fillna(df['age'].mean(), inplace=True)
df['city'].fillna('Unknown', inplace=True)
print("\nDataFrame after filling missing values:")
print(df)
df['city'].fillna(method='ffill', inplace=True)
print("\nDataFrame after forward filling 'city':")
print(df)
print("\nFinal DataFrame:")
print(df)
