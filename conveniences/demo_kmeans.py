#
# demo_kmeans.py
#

import kmeans
import numpy as np
import matplotlib.pyplot as plt

data = []
number_of_clusters = 5
points_per_cluster = 25


np.random.seed(4)

'''
Generate random clusters.
'''

for _ in range(number_of_clusters):

    ages_centroid = np.random.uniform(20.0, 70.0)
    income_centroid = np.random.uniform(100000.0, 500000.0)

    age = np.random.normal(ages_centroid, 2.0, points_per_cluster)
    income = np.random.normal(income_centroid, 10000.0, points_per_cluster)
    points = [[age[i], income[i]] for i in range(len(age))]

    data.extend(points)

'''
Use k-means to identify the clusters and compute their centroids.
'''

centroids, assignments, data = kmeans.centroids(k=5, data=data, max_iterations=100000)

'''
Assign each data point a color associated to their respective cluster.
'''

colors = ['blue', 'green', 'purple', 'orange', 'pink']

for i in range(len(data)):

    data[i].append(colors[assignments[i]])

'''
Plot the data points colored to represent the cluster they belong to.
'''

ages = [x[0] for x in data]
incomes = [x[1] for x in data]
colors = [x[2] for x in data]

centroids_x = [x[0] for x in centroids]
centroids_y = [y[1] for y in centroids]

plt.xlabel('age')
plt.ylabel('income')
plt.scatter(ages, incomes, c=colors)
plt.scatter(centroids_x, centroids_y, c='red')
plt.show()
