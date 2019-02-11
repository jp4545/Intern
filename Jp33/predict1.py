'''
Jaya Prakash - 33
Train program to predict numbers using train.csv file
Working
'''

import numpy as np
import matplotlib.pyplot as pt 
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
data = pd.read_csv("train.csv").as_matrix()
clf = DecisionTreeClassifier()

xtrain = data[0:21000,1:]
trainlbe = data[0:21000,0]
clf.fit(xtrain,trainlbe)

xtest = data[21000:,1:]
actual_lable = data[21000:,0]
 
d = xtest[7]
d.shape=(28,28)
pt.imshow(255-d,cmap = 'gray')
print(clf.predict( [xtest[7]]))
pt.show()

