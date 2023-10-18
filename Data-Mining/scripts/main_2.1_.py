import scipy.io
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import DBSCAN

# Step 1. Load the dataset 'mydata' from the data file 'mydata.mat'.
mat_file = scipy.io.loadmat('mydata.mat')
X = np.array(mat_file['X'])

# Step 2. Execute the DBSCAN method for the first two dimensions of the X array, providing values
# for the algorithm's parameters: ε=0.5 and MinPts=15.
dbscan = DBSCAN(eps=0.5, min_samples=15).fit(X)
IDX = dbscan.labels_

# Step 3. Present a scatter plot of the values of the two dimensions of the X array.
plt.figure(1)
plt.scatter(X[:, 0], X[:, 1])
plt.savefig('2.1 Step 3.png', bbox_inches='tight')
plt.show()

# Step 4. Present a second plot that shows the clusters to which the DBSCAN method assigned the data points,
# as well as the noise points.
plt.figure(1)
plt.scatter(X[:, 0], X[:, 1], c=IDX)
plt.savefig('2.1 Step 4.png', bbox_inches='tight')
plt.show()
