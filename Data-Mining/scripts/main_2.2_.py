from sklearn.datasets import load_iris
import matplotlib.pyplot as plt
from scipy.stats import zscore
from sklearn.cluster import DBSCAN

# Step 1. Load the Iris dataset from the data file and use only dimensions [2,3].
meas = load_iris().data
X = meas[:, [2, 3]]

# Step 2. Execute the DBSCAN method for the first two dimensions of the X array, providing values
# for the algorithm's parameters: ε=0.1 and MinPts=5.
dbscan = DBSCAN(eps=0.1, min_samples=5).fit(X)
IDX = dbscan.labels_

# Step 3. Present a scatter plot of the values of the two dimensions of the X array.
plt.figure(1)
plt.scatter(X[:, 0], X[:, 1])
plt.savefig('2.2 Step 3.png', bbox_inches='tight')
plt.show()

# Step 4. Present a second plot that shows the clusters to which the DBSCAN method assigned the data points,
# as well as the noise points.
plt.figure(1)
plt.scatter(X[:, 0], X[:, 1], c=IDX)
plt.savefig('2.2 Step 4.png',  bbox_inches='tight')
plt.show()

# Step 5. Repeat the above process after normalizing the data in the X array using the zscore method.
# Comment on the result.
xV1 = zscore(X[:, 0])
xV2 = zscore(X[:, 1])
X = [xV1, xV2]
dbscan = DBSCAN(eps=0.1, min_samples=5).fit(X)
IDX = dbscan.labels_
plt.figure(1)
plt.scatter(xV1, xV2)
plt.savefig('2.2 Step 5.png',  bbox_inches='tight')
plt.show()
