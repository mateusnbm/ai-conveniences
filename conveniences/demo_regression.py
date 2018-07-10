#
# demo_regression.py
#

import csv
import regression
import matplotlib.pyplot as plt

file = open('../datasets/swedish_insurance.csv')
data = list(csv.reader(file))

claims = [float(item[0]) for item in data]
amounts = [float(item[1]) for item in data]

slope, intercept, r_squared = regression.linear_regression(claims, amounts)
predictions = [regression.linear_regression_predict(slope, intercept, k) for k in claims]

print('')
print('slope: ' + str(slope))
print('intercept: ' + str(intercept))
print('r-squared: ' + str(r_squared))
print('')

plt.xlabel('claims')
plt.ylabel('amount')
plt.scatter(claims, amounts)
plt.plot(claims, predictions, 'r')
plt.show()

file.close()
