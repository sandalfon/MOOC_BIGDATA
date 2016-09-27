# -*- coding: utf-8 -*-
"""
Created on Tue Sep 27 13:04:19 2016

@author: gvieira
"""

import numpy as np

y = np.array([1,1,1,1,1,1,1,1])

I=np.identity(8)

E=np.zeros((8,8))
E[0,7]=1
X=I+E
beta=np.linalg.inv(X.transpose().dot(X)).dot(X.transpose()).dot(y)

res=np.sum(beta)

print(res)