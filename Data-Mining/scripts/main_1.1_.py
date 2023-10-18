from sklearn.datasets import load_iris
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

# Step 1. Load the Iris dataset.
meas = load_iris().data
# Step 2. Execute the k-means algorithm using Euclidean distance.
# Using the last two dimensions of the array.
X = meas[:, [2, 3]]
k = 3  # Define that the data will be organized into 3 clusters.
kmeans = KMeans(n_clusters=k).fit(X)  # Apply k-means
IDX = kmeans.labels_
C = kmeans.cluster_centers_
# Step 3. Present the data in a graph.
plt.figure(1)
# Display the class to which each observation belongs.
plt.plot(IDX[:], 'o')
plt.show()
plt.plot(X[IDX == 0][:, 0], X[IDX == 0][:, 1], 'limegreen', marker='o', linewidth=0, label='C1')
plt.plot(X[IDX == 1][:, 0], X[IDX == 1][:, 1], 'yellow', marker='o', linewidth=0, label='C2')
plt.plot(X[IDX == 2][:, 0], X[IDX == 2][:, 1], 'c.', marker='o', label='C3')
plt.scatter(C[:, 0], C[:, 1], marker='x', color='black', s=150, linewidth=3, label="Centroids", zorder=10)
plt.legend()
plt.savefig('1.1 Step 3.png', bbox_inches='tight')
plt.show()
# Step 4. Using SSE and silhouette score as evaluation criteria,
# examine the effect of k on clustering. For the best combination of features,
# plot the relationship between k and SSE.
sse = []
contour_coefficient = []

for k in range(2, 11):
    kmeans = KMeans(n_clusters=k, random_state=0).fit(X)
    sse.append(kmeans.inertia_)
    contour_coefficient.append(silhouette_score(meas, kmeans.labels_))

plt.plot(range(2, 11), sse)
plt.xlabel("Number of K")
plt.ylabel("SSE")
plt.savefig('1.1 Step 4.png', bbox_inches='tight')
plt.show()
