# Data Mining Project: Clustering Analysis

## Overview
This project involves the application of clustering algorithms to different datasets, analyzing the effect of the number of clusters (k) on clustering quality, and comparing the results. Two datasets, iris and xV.mat, are used with the k-means and DBSCAN algorithms. The results are presented through visualizations and evaluations.

## Dataset Description
### 1.1 Application to the Iris Dataset
#### Step 1: Load the Iris dataset.
#### Step 2: Apply the k-means algorithm with Euclidean distance.
#### Step 3: Plot the data.
#### Step 4: Analyze the effect of varying 'k' on clustering using SSE and silhouette coefficient. Plot the relationship between 'k' and SSE.

### 1.2 Application to the xV.mat Dataset
### Step 1: Load the xV dataset from the 'xV.mat' file, containing 600 samples with 469 features.
#### Step 2: Apply k-means clustering with Euclidean distance for 3 clusters using the first two features of the xV matrix. Calculate SSE.
#### Step 3: Apply k-means clustering with Euclidean distance for 3 clusters using features [296, 305] of the xV matrix. Calculate SSE.
#### Step 4: Repeat Step 3 using the last two features of the xV matrix.
#### Step 5: Repeat Step 3 for 3 clusters using the features [205, 175] of the xV matrix. Calculate SSE.
#### Step 6: Compare the results from Steps 2, 4, and 5.

### 2.1 Application to the mydata Dataset
#### Step 1: Load the 'mydata' dataset from the 'mydata.mat' file.
#### Step 2: Run the DBSCAN method for the first two dimensions of the X matrix with parameters ε=0.5 and MinPts=15.
#### Step 3: Plot the values of the two dimensions of the X matrix.
#### Step 4: Present the clusters created by the DBSCAN method and visualize the noise.

### 2.2 Application to the Iris Dataset
#### Step 1: Load the Iris dataset.
#### Step 2: Run the DBSCAN method for the first two dimensions of the X matrix with parameters ε=0.1 and MinPts=5.
#### Step 3: Plot the values of the two dimensions of the X matrix.
#### Step 4: Present the clusters created by the DBSCAN method and visualize the noise.
#### Step 5: Repeat the above procedure after normalizing the data using the zscore method.

## Code Implementation
You can find the code for each of the above steps in separate Python scripts:
- `main_1.1.py` for 1.1
- `main_1.2.py` for 1.2
- `main_2.1.py` for 2.1
- `main_2.2.py` for 2.2

The code contains explanations and detailed steps to perform the tasks described in the project.

Please ensure you have the required Python (ver. 3.10.5) libraries, such as scikit-learn, NumPy, SciPy, and Matplotlib, installed in your environment before running the code.
```
scikit-learn==1.2.0
numpy==1.24.1
scipy==1.10.0
matplotlib==3.6.3
```

You can install these libraries using pip by running:
```
pip install -r requirements.txt
```

## Usage
1. Load the specified datasets for each part of the project.
2. Run the provided Python scripts (`main.py`) to perform the tasks.
3. Analyze the results, including visualizations and evaluations, to gain insights into the clustering outcomes.
4. Adjust parameters or features as needed for further analysis.


**Note:** Ensure that the required datasets, 'xV.mat' and 'mydata.mat', are available in your project directory or update the file paths in the code as necessary.
