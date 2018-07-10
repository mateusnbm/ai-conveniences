#
# statistics.py
#

import copy
import math
import numpy
import quicksort

def mean(data):

    return sum(data)/len(data)

def median(data):

    index = len(data)//2
    is_odd = len(data) % 2 > 0
    data = quicksort.sort(copy.deepcopy(data))

    return data[index] if is_odd else (data[index]+data[index-1])/2

def mode(data):

    lookup = {}

    for n in data: lookup[n] = 0
    for n in data: lookup[n] += 1

    return sorted(lookup, key=lookup.__getitem__)[-1]

def standard_deviation(data=[], is_sample=False):

    dmean = mean(data)
    diffs = [math.pow(n-dmean, 2) for n in data]
    divisor = len(data)-1 if is_sample else len(data)

    return math.sqrt(sum(diffs)/divisor)

def variance(data, is_sample=False):

    return math.pow(standard_deviation(data, is_sample), 2)

def covariance(x=[], y=[], is_sample=False):

    xmean = mean(x)
    ymean = mean(y)

    xvect = [(n-xmean) for n in x]
    yvect = [(n-ymean) for n in y]

    divisor = len(x)-1 if is_sample else len(x)
    result = numpy.dot(xvect, yvect) / divisor

    return result

def correlation(x=[], y=[], is_sample=False):

    xstd = standard_deviation(x, is_sample)
    ystd = standard_deviation(y, is_sample)

    return covariance(x, y, is_sample) / xstd / ystd
