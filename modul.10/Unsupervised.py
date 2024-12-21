import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# Read the dataset
data = pd.read_csv('modul.10/iris.csv')
x = data.drop('species', axis=1)

# Standardize the dataset
scaler = StandardScaler()
x_scaled = scaler.fit_transform(x)

# Train the model
KMeans = KMeans(n_clusters=3, random_state=42)
KMeans.fit(x_scaled)

# Predict the cluster
y_kmeans = KMeans.predict(x_scaled)

# visualize the cluster
plt.scatter(x_scaled[y_kmeans == 0, 0], x_scaled[y_kmeans == 0, 1], s=100, c='red', label='Cluster 1')
plt.scatter(x_scaled[y_kmeans == 1, 0], x_scaled[y_kmeans == 1, 1], s=100, c='blue', label='Cluster 2')
plt.scatter(x_scaled[y_kmeans == 2, 0], x_scaled[y_kmeans == 2, 1], s=100, c='green', label='Cluster 3')
plt.scatter(x_scaled[:, 0], x_scaled[:, 1], c=y_kmeans, cmap='viridis', label='Centroids')
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Sepal Width (cm)')
plt.title('KMeans Clustering')
plt.show()