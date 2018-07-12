#
# kmeans.py
#

import copy
import math
import random

def __euclidean_distance__(a, b):

    return math.sqrt(sum([pow(a[i]-b[i], 2) for i in range(len(a))]))

def __centroids__(k, data):

    centroids = [[] for _ in range(k)]
    dimensionality = len(data[0])

    for w in range(dimensionality):

        vals = [item[w] for item in data]
        vmin = min(vals)
        vmax = max(vals)

        for z in range(k):

            centroids[z].append(random.uniform(vmin, vmax))

    return centroids

def __closest_point__(centroids, point):

    index = 0
    min_distance = __euclidean_distance__(point, centroids[0])

    for j in range(len(centroids)):

        distance = __euclidean_distance__(point, centroids[j])

        if min_distance > distance:

            index = j
            min_distance = distance

    return index

def __normalize__(data):

    for i in range(len(data[0])):

        values = [x[i] for x in data]
        vmin = min(values)
        vmax = max(values)

        for point in data:

            point[i] = (point[i]-vmin)/(vmax-vmin)

    return data

def centroids(k=1, data=[], max_iterations=1000):

    iteration = 0
    assigned = True

    # First we need to normalize the data in order to guaratee that each
    # attribute will have the same impact when calculating the distances.

    data = __normalize__(copy.deepcopy(data))
    centroids = __centroids__(k, data)
    assignments = [0 for _ in range(len(data))]

    # Main algorithm loop. Keep updating the centroids while they don't
    # change or the maximum number of iterations is reached.

    while iteration < max_iterations and assigned == True:

        iteration += 1
        assigned = False
        clusters = [[] for _ in range(k)]

        # Assign each data point to a cluster.

        for i in range(len(data)):

            cluster_index = __closest_point__(centroids, data[i])
            clusters[cluster_index].append(data[i])

            if assignments[i] != cluster_index:

                assigned = True
                assignments[i] = cluster_index

        # Average the points belonging to a cluster and re-compute the centroid.

        for i in range(k):

            n = len(data[0])
            centroid = [0 for _ in range(n)]

            for point in clusters[i]:

                for w in range(n):

                    centroid[w] += point[w]

            n = len(clusters[i])
            n = 1 if n == 0 else n
            centroid = [(x/n) for x in centroid]
            centroids[i] = centroid

    return centroids, assignments, data
