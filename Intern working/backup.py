clf = DecisionTreeClassifier()

xtrain = data[0:21000,1:]
trainlbe = data[0:21000,0]
clf.fit(xtrain,trainlbe)

xtest = data[21000:,1:]
actual_lable = data[21000:,0]
d = xtest
p = clf.predict(xtest)
pt.imshow(255-d,cmap = 'gray')
print(p)
