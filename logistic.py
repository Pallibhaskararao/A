import pandas as pd
df = pd.read_csv("Heart.csv")
df = df.drop(columns = 'Unnamed: 0')

df['ChestPain'] = df['ChestPain'].astype('category')
df['ChestPain'] = df['ChestPain'].cat.codes
df['Thal'] = df['Thal'].astype('category')
df['Thal'] = df['Thal'].cat.codes
df['AHD'] = df['AHD'].astype('category')
df['AHD'] = df['AHD'].cat.codes

print(df.isnull().sum())
df = df.dropna()
X = df.drop(columns = 'AHD', axis = 1)
y = df['AHD']

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=45)
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
X_train_Scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

from sklearn.linear_model import LogisticRegression
LOR = LogisticRegression()
LOR.fit(X_train_Scaled, y_train)
y_pred = LOR.predict(X_test_scaled)
print(y_pred)
