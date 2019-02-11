import numpy as np
import matplotlib.pyplot as pt
from skimage.io import imread
from skimage.transform import resize 
import pandas as pd
import os
from sklearn.tree import DecisionTreeClassifier
img = "jj.jpg"
imgrd = imread(img)

print(imgrd)