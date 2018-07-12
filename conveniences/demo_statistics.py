#
# demo_statistics.py
#

import numpy
import random
import statistics
import matplotlib.pyplot as plt

'''
Calculate the mean, mode, median, standard deviation and variance.
'''

data = numpy.random.normal(1, 0.5, 10000)

mean = statistics.mean(data)
mode = statistics.mode(data)
median = statistics.median(data)
std = statistics.standard_deviation(data)
variance = statistics.variance(data)

print('')
print('Mean: ' + str(mean))
print('Mode: ' + str(mode))
print('Median: ' + str(median))
print('Standard Variance: ' + str(std))
print('Variance: ' + str(variance))

plt.xlabel('value')
plt.ylabel('count')
plt.hist(data, 50)
plt.show()

'''
Calculate the covariance of uncorrelated data.
'''

ages = numpy.random.normal(50.0, 10.0, 1000)
income = numpy.random.normal(100000.0, 75000.0, 1000)

covariance = statistics.covariance(ages, income, is_sample=True)
correlation = statistics.correlation(ages, income, is_sample=True)

print('')
print('Uncorrelated data.')
print('Covariance: ' + str(covariance))
print('Correlation: ' + str(correlation))

plt.xlabel('age')
plt.ylabel('income')
plt.scatter(ages, income)
plt.show()

'''
Calculate the covariance and correlation of data known to be correlated.
'''

ages = numpy.random.normal(50.0, 10.0, 1000)
income = [(n*1000+random.uniform(0, n/1000)*500000) for n in ages]

covariance = statistics.covariance(ages, income, is_sample=True)
correlation = statistics.correlation(ages, income, is_sample=True)

print('')
print('Correlated data.')
print('Covariance: ' + str(covariance))
print('Correlation: ' + str(correlation))

plt.xlabel('age')
plt.ylabel('income')
plt.scatter(ages, income)
plt.show()

print('')
