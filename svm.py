from sklearn import datasets,svm,metrics
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt
cancer=datasets.load_breast_cancer()
data,target=cancer.data,cancer.target
print(f"data shape :{data.shape}")
print(f"target shape:{target.shape}")
print(f"feature name:{cancer.feature_names}")
c=svm.SVC(gamma=0.001)
x_train,x_test,y_train,y_test=train_test_split(data,target,test_size=0.5,shuffle=True,random_state=42)
c.fit(x_train,y_train)
predict=c.predict(x_test)
print(f"classification report for classifier{c}:")
print(metrics.classification_report(y_test,predict))
accuracy=accuracy_score(y_test,predict)
print("accuracy:",f"{accuracy*100:.2f}")
