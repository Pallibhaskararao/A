#Bar graph
from matplotlib import pyplot as p
x=[1,2,5,4,7]
y=[3,4,1,6,7]
p.bar(x,y)
p.show()


#Stem
from matplotlib import pyplot as p
x=[1,2,5,4,7]
y=[3,4,1,6,7]
p.stem(x,y)
p.show()


#Scatter plot
from matplotlib import pyplot as p
x=[1,2,5,4,7]
y=[3,4,1,6,7]
p.scatter(x,y)
p.show()


#Line plot
from matplotlib import pyplot as p
x=[1,2,5,4,7]
y=[3,4,1,6,7]
p.plot(x,y)
p.title("line plot")
p.legend(["graph"])
p.show()


#Histogram 
import pandas as pd
values = pd.DataFrame({
  'Length': [2.7,9],
  'Breadth': [4.24, 2.67]
})
hist = values.hist(bins=5)


#Pie chart
import matplotlib.pyplot as plt
subjects = ['ATCD', 'DBMS', 'OS', 'AITT', 'DAA']
marks = [85, 78, 82, 90, 88]
plt.pie(marks, labels=subjects, autopct='%1.1f%%')
plt.title('Students Marks in Different Subjects')
plt.axis('equal')
plt.show()
