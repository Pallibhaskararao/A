from sklearn.datasets import load_iris
import pandas as pd
iris = load_iris()
iris_df=pd.DataFrame(data=iris.data,
                         columns=iris.feature_names)
iris_df['species']= pd.Categorical.from_codes(iris.target,            
                          iris.target_names)
print(iris_df.head())
print(iris_df.describe())
