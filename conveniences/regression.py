#
# regression.py
#
# Based-on:
#
# https://en.wikipedia.org/wiki/Coefficient_of_determination
# https://machinelearningmastery.com/implement-simple-linear-regression-scratch-python/
# https://www.udemy.com/data-science-and-machine-learning-with-python-hands-on/
#

import statistics

def linear_regression_predict(slope, intercept, k):

	return slope * k + intercept

def linear_regression(x, y):

	x_mean = statistics.mean(x)
	y_mean = statistics.mean(y)

	a = statistics.covariance(x, y)
	b = statistics.variance(x, x_mean)

	slope = a / b
	intercept = y_mean - slope * x_mean

	sum_of_squares = 0
	sum_of_squares_of_residuals = 0

	for i in range(len(x)):

		x_value = x[i]
		y_value = y[i]
		predicted = linear_regression_predict(slope, intercept, x_value)

		sum_of_squares += pow((y_value-y_mean), 2)
		sum_of_squares_of_residuals = pow((y_value-predicted), 2)

	r_squared = 1-(sum_of_squares_of_residuals/sum_of_squares)

	return slope, intercept, r_squared
