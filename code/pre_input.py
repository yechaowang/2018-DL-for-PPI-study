# Written by Alex_Wong in python
# time 2018.4.21 13:45 
# verson 1.0


import numpy as np
import os
import string
from numpy import *
from numpy import linalg as LA
import sklearn
from sklearn import preprocessing
dic = {'A': [0.62, -0.5, 0.007187, 8.1, 0.046, 1.181, 27.5], 
'C': [0.29, -1, -0.03661, 5.5, 0.128, 1.461, 44.6], 
'D': [-0.9, 3, -0.02382, 13, 0.105, 1.587, 40], 
'E': [-0.74, 3, 0.006802, 12.3, 0.151, 1.862, 62], 
'F': [1.19, -2.5, 0.037552, 5.2, 0.29, 2.228, 115.5], 
'G': [0.48, 0, 0.179052, 9, 0, 0.881, 0], 
'H': [-0.4, -0.5, -0.01069, 10.4, 0.23, 2.025, 79], 
'I': [1.38, -1.8, 0.021631, 5.2, 0.186, 1.81, 93.5], 
'K': [-1.5, 3, 0.017708, 11.3, 0.219, 2.258, 100], 
'L': [1.06, -1.8, 0.051672, 4.9, 0.186, 1.931, 93.5], 
'M': [0.64, -1.3, 0.002683, 5.7, 0.221, 2.034, 94.1], 
'N': [-0.78, 2, 0.005392, 11.6, 0.134, 1.655, 58.7], 
'P': [0.12, 0, 0.239531, 8, 0.131, 1.468, 41.9], 
'Q': [-0.85, 0.2, 0.049211, 10.5, 0.18, 1.932, 80.7], 
'R': [-2.53, 3, 0.043587, 10.5, 0.291, 2.56, 105], 
'S': [-0.18, 0.3, 0.004627, 9.2, 0.062, 1.298, 29.3], 
'T': [-0.05, -0.4, 0.003352, 8.6, 0.108, 1.525, 51.3], 
'V': [1.08, -1.5, 0.057004, 5.9, 0.14, 1.645, 71.5], 
'W': [0.81, -3.4, 0.037977, 5.4, 0.409, 2.663, 145.5], 
'Y': [0.26, -2.3, 117.3, 6.2, 0.298, 2.368, 0.023599]}


count = 0
sumx = []
tmplist = []
tmpout = []
outarray = []
def autocov(inputmat, num, iterator, averagemat):
	tmpout = []
	outarray = []
	for j in range(0,iterator):
		for n in range(0,num-j):
			tmpout =+ (multiply((tmparray[n]-averagemat), (tmparray[n+j]-averagemat)))/(num-j)
		outarray.append(tmpout)
	outarray1 = array(outarray)
	sklearn.preprocessing.normalize(outarray1, norm='l2')
	print (outarray1.shape)
	return outarray1

with open('test.txt', 'r') as file:
	for line in file:
		lst = list(line)
		length = len(lst)	
		if lst[0].isalpha():
			for i in range(0, length):
				if lst[i] == '\n':
					break
				tmplist.append((dic[lst[i]]))
				count = count + 1
			tmparray = np.array(tmplist)
			sumx = tmparray.sum(axis = 0)
#			print (sumx)
			print ('\n\n')
#			print (len(tmparray))
			autocov(tmparray, count, 30, sumx)
			count = 0
			sumx = []
			tmplist = []

file.close()





