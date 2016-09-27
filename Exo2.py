# -*- coding: utf-8 -*-
"""
Created on Tue Sep 27 13:23:14 2016

@author: gvieira
"""

import numpy as np

X=np.zeros((4898,11))
y=np.zeros(4898)


r = np.genfromtxt('data/winequality-white.csv',delimiter=';',dtype=float, names=True,autostrip=True)
for i in range (0,4898):
    y[i]=r[i][11]
    for j in range(0,11):
        X[i,j]=r[i][j]


beta=np.linalg.inv(X.transpose().dot(X)).dot(X.transpose()).dot(y)

eqr=(X.dot(beta)-y).dot(X.dot(beta)-y)