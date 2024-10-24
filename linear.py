SIMPLE REGRESSION : 
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt


df = pd.read_csv('used_cars.csv')
df = df.head(50)
df.isnull().sum()


df1 = df[['milage', 'price']]
df1.loc[:, 'milage'] = df1['milage'].str.replace(',', '').str.replace(' mi', '').astype(float)
df1.loc[:, 'price'] = df1['price'].str.replace('$', '').str.replace(',', '').astype(float)


X = df1.drop('price', axis=1)
y = df1['price']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


LR = LinearRegression()
LR.fit(X_train, y_train)
print("The intercept value is :",LR.intercept_)
print("The coefficient value is : ",LR.coef_)
Y_test = LR.predict(X_test)
print(Y_test)


plt.scatter(X_train, y_train, color='blue', label='Training data')
y_train_pred = LR.predict(X_train)


plt.plot(X_train.values, y_train_pred, color='red', label='Best fit line')
plt.xlabel('Milage (miles)')
plt.ylabel('Price (rupees)')
plt.title('Milage vs. Price (Training Data)')
plt.legend()
plt.show()
MULTIPLE REGRESSION : 


import pandas as pd
df = pd.read_csv('insurance.csv')
print(df.head())
df['sex'] = df['sex'].astype('category')
df['sex'] = df['sex'].cat.codes
df['smoker'] = df['smoker'].astype('category')
df['smoker'] = df['smoker'].cat.codes
df['region'] = df['region'].astype('category')
df['region'] = df['region'].cat.codes
df.isnull().sum()
x = df.drop(columns = 'charges')
y = df['charges']


from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size = 0.2,random_state = 23)


from sklearn.linear_model import LinearRegression
LR = LinearRegression()
LR.fit(x_train,y_train)
c = LR.intercept_
m = LR.coef_
print("The intercept is : ",c)
print("The coefficients : ", m)
y_pred_test = LR.predict(x_test)
print(y_pred_test)


import matplotlib.pyplot as plt
plt.scatter(y_test,y_pred_test,c = 'red')
plt.xlabel("actual charges")
plt.ylabel("predicted charges")
plt.show()
