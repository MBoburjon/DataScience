from numpy import random, array
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from sklearn.preprocessing import scale
from numpy import random, float


#create fake income/age clusters fro N people in k clusters
def createClusteredData(N, k):
	random.seed(10)
	pointsPerCluster = float(N)/k
	X = []
	for x in range (k):
		incomeCentroid = random.uniform(2000.0, 200000.0)
		ageCentroid = random.uniform(20.0, 70.0)
		for j in range(int(pointsPerCluster)):
			X.append([random.normal(incomeCentroid, 10000.0), 
				random.normal(ageCentroid, 2.0)])
	X = array(X)
	return X

data = createClusteredData(100, 5)

model = KMeans(n_clusters=5)

#Note I'm normalizing data using scale funtion. its important to get good result
model = model.fit(scale(data))

#prints each data clusters that each data point was assigned
print(model.labels_)

#finally visualize items
plt.figure(figsize=(8,6))
plt.scatter(data[:,0], data[:,1], c=model.labels_.astype(float))
plt.show()

