import numpy as np
import matplotlib.pyplot as pt 
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
data = pd.read_csv("jpj.csv").as_matrix()
clf = DecisionTreeClassifier()

xtrain = data[0:21000,1:]
trainlbe = data[0:21000,0]
clf.fit(xtrain,trainlbe)

xtest = data[21000:,1:]
actual_lable = data[21000:,0]
 
p = clf.predict(xtest)
c = 0
for i in range(1,21000):
	 if p[i]==actual_lable[i]:
	 		 c+=1
	 else:
	 	 	 print("0")
print("Accuracy=",(c/21000)*100)