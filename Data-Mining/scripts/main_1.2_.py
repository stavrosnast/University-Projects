import math
import scipy.io
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# Step 1. Load the dataset xV from the data file 'xV.mat,' which contains 600 samples
# with 469 features each.
mat_file = scipy.io.loadmat('xV.mat')
xV = np.array(mat_file['xV'])
# Step 2. Perform clustering using the k-means algorithm with Euclidean distance for 3 clusters,
# using the first two features of the xV array. Calculate SSE.
X = xV[:, [0, 1]]
k = 3
kmeans = KMeans(n_clusters=k).fit(X)
IDX = kmeans.labels_
C = kmeans.cluster_centers_
plt.plot(X[IDX == 0][:, 0], X[IDX == 0][:, 1], 'limegreen', marker='o', linewidth=0, label='C1')
plt.plot(X[IDX == 1][:, 0], X[IDX == 1][:, 1], 'yellow', marker='o', linewidth=0, label='C2')
plt.plot(X[IDX == 2][:, 0], X[IDX == 2][:, 1], 'c.', marker='o', label='C3')
plt.scatter(C[:, 0], C[:, 1], marker='x', color='black', s=150, linewidth=3, label="Centroids", zorder=10)
plt.legend()
plt.savefig('1.2 Step 2.png', bbox_inches='tight')
plt.show()
# Calculate SSE
sse = 0.0
numberOfRows, numberOfColumns = X.shape
for i in range(k):
    plt.plot(X[IDX == i][:, 0], X[IDX == i][:, 1], marker='o', linewidth=0, label=i + 1)
    for j in range(numberOfRows):
        if IDX[j] == i:
            sse = sse + math.dist(X[j], C[i]) ** 2
print("\n\nSSE Step 2 = %.3f" % sse)

# Step 3. Perform clustering using the k-means algorithm with Euclidean distance for 3 clusters,
# using features [296, 305] of the xV array. Calculate SSE.
X = xV[:, [296, 305]]
k = 3
kmeans = KMeans(n_clusters=k).fit(X)
IDX = kmeans labels_
C = kmeans.cluster_centers_
plt.plot(X[IDX == 0][:, 0], X[IDX == 0][:, 1], 'limegreen', marker='o', linewidth=0, label='C1')
plt.plot(X[IDX == 1][:, 0], X[IDX == 1][:, 1], 'yellow', marker='o', linewidth=0, label='C2')
plt.plot(X[IDX == 2][:, 0], X[IDX == 2][:, 1], 'c.', marker='o', label='C3')
plt.scatter(C[:, 0], C[:, 1], marker='x', color='black', s=150, linewidth=3, label="Centroids", zorder=10)
plt.legend()
plt.savefig('1.2 Step 3.png', bbox_inches='tight')
plt.show()
# Calculate SSE
sse = 0.0
numberOfRows, numberOfColumns = X.shape
for i in range(k):
    plt.plot(X[IDX == i][:, 0], X[IDX == i][:, 1], marker='o', linewidth=0, label=i + 1)
    for j in range(numberOfRows):
        if IDX[j] == i:
            sse = sse + math.dist(X[j], C[i]) ** 2
print("\n\nSSE Step 3 = %.3f" % sse)

# Step 4. Repeat Step 3 using the last two features of the xV array.
X = xV[:,-2:]
k = 3
kmeans = KMeans(n_clusters=k).fit(X)
IDX = kmeans.labels_
C = kmeans.cluster_centers_
plt.plot(X[IDX == 0][:, 0], X[IDX == 0][:, 1], 'limegreen', marker='o', linewidth=0, label='C1')
plt.plot(X[IDX == 1][:, 0], X[IDX == 1][:, 1], 'yellow', marker='o', linewidth=0, label='C2')
plt.plot(X[IDX == 2][:, 0], X[IDX == 2][:, 1], 'c.', marker='o', label='C3')
plt.scatter(C[:, 0], C[:, 1], marker='x', color='black', s=150, linewidth=3, label="Centroids", zorder=10)
plt.legend()
plt.savefig('1.2 Step 4.png', bbox_inches='tight')
plt.show()
# Calculate SSE
sse = 0.0
numberOfRows, numberOfColumns = X.shape
for i in range(k):
    plt.plot(X[IDX == i][:, 0], X[IDX == i][:, 1], marker='o', linewidth=0, label=i + 1)
    for j in range(numberOfRows):
        if IDX[j] == i:
            sse = sse + math.dist(X[j], C[i]) ** 2
print("\n\nSSE Step 4 = %.3f" % sse)

# Step 5. Repeat Step 3 for 3 clusters using features [205, 175] of the xV array. Calculate SSE.
X = xV[:, [205, 175]]
k = 3
kmeans = KMeans(n_clusters=k).fit(X)
IDX = kmeans.labels_
C = kmeans.cluster_centers_
plt.plot(X[IDX == 0][:, 0], X[IDX == 0][:, 1], 'limegreen', marker='o', linewidth=0, label='C1')
plt.plot(X[IDX == 1][:', 0], X[IDX == 1][:, 1], 'yellow', marker='o', linewidth=0, label='C2')
plt.plot(X[IDX == 2][:, 0], X[IDX == 2][:, 1], 'c.', marker='o', label='C3')
plt.scatter(C[:, 0], C[:, 1], marker='x', color='black', s=150, linewidth=3, label="Centroids", zorder=10)
plt.legend()
plt.savefig('1.2 Step 5.png', bbox_inches='tight')
plt.show()
# Calculate SSE
sse = 0.0
numberOfRows, numberOfColumns = X.shape
for i in range(k):
    plt.plot(X[IDX == i][:, 0], X[IDX == i][:, 1], marker='o', linewidth=0, label=i + 1)
    for j in range(numberOfRows):
        if IDX[j] == i:
            sse = sse + math.dist(X[j], C[i]) ** 2
print("\n\nSSE Step 5 = %.3f" % sse)
