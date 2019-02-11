import sys
reload(sys)
sys.setdefaultencoding('ISO-8859-1')
import numpy as np
import matplotlib.pyplot as pt 
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
data = pd.read_csv("jpj.csv").as_matrix()
clf = DecisionTreeClassifier()

print(data)