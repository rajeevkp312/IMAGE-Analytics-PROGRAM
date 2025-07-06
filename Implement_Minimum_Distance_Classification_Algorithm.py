import numpy as np
from sklearn.datasets import make_blobs

# Generate data
X, y = make_blobs(n_samples=100, centers=3)

# Calculate class centers
centers = [X[y==k].mean(axis=0) for k in np.unique(y)]

# Classify new point
new_point = [0, 0]
closest_class = np.argmin([np.linalg.norm(new_point - c) for c in centers])
print(f"Class: {closest_class}")