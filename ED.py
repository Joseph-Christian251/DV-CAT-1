from scipy.spatial.distance import euclidean
# Data
X = [
    [5.1,3.5,1.4,0.2],
    [4.9,3.0,1.4,0.2],
    [6.2,3.4,5.4,2.3],
    [5.9,3.0,5.1,1.8],
    [5.6,2.9,3.6,1.3],
    [5.7,2.8,4.1,1.3]
]


d = euclidean(X[0], X[1])
print("Distance between M001 and M002:", d)