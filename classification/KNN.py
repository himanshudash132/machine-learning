# # Loading requied modules
# from sklearn import datasets
# from sklearn.neighbors import KNeighborsClassifier

# # Loading Dataset
# iris = datasets.load_iris()

# # Printing features and labels
# features = iris.data
# labels = iris.target
# #print(iris.DESCR)

# # print(features[0], labels[0])

# # Training the classifier

# clf = KNeighborsClassifier()
# clf.fit(features, labels)

# preds = clf.predict([[9.1, 9,5, 6.4, 0.2]])
# print(preds)
# Loading required modules
from sklearn import datasets
from sklearn.neighbors import KNeighborsClassifier

# Loading Dataset
iris  = datasets.load_iris()

# Printing features and labels
features = iris.data
labels = iris.target
# print(iris.DESCR)

print(features[0],labels[0])

# Training the classifier

clf = KNeighborsClassifier()
clf.fit(features, labels)

preds = clf.predict([[9.1, 9.5, 6.4, 0.2]])
print(preds)
