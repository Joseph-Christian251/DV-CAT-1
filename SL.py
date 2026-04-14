from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

# Data
X = [
    [5.1,3.5,1.4,0.2],
    [4.9,3.0,1.4,0.2],
    [6.2,3.4,5.4,2.3],
    [5.9,3.0,5.1,1.8],
    [5.6,2.9,3.6,1.3],
    [5.7,2.8,4.1,1.3]
]

y = ["Setosa","Setosa","Virginica","Virginica","Versicolor","Versicolor"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = KNeighborsClassifier(n_neighbors=3)
model.fit(X_train, y_train)

print("Accuracy:", model.score(X_test, y_test))