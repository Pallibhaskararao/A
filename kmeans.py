import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans


np.random.seed(0)
X = np.random.rand(100, 2)
k = 3
kmeans = KMeans(n_clusters=k)
kmeans.fit(X)


labels = kmeans.labels_
centroids = kmeans.cluster_centers_


plt.scatter(X[:, 0], X[:, 1], c=labels, cmap='viridis', marker='o', edgecolor='k')
plt.scatter(centroids[:, 0], centroids[:, 1], c='red', marker='X', s=200, label='Centroids')
plt.title('K-means Clustering')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.legend()
plt.grid()
plt.show()
