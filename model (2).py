# -*- coding: utf-8 -*-
"""
Created on Tue Aug 15 13:49:50 2023

@author: SRIRAM
"""
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
exp=(3,2,1,7,8,2,10,14,11,)
salary=(30000,27000,25000,45000,46500,26000,47000,65000,50000)
exp=np.array(exp).reshape(-1, 1)
x=int(input('years'))
print(exp)
salary=np.array(salary).reshape(-1, 1)

Ir=LinearRegression()
Ir.fit(exp,salary)
salary_pred=Ir.predict([[x]])
print(salary_pred)

mse=mean_squared_error(salary,salary_pred)
rmse=np.sqrt(mse)
r2_score=Ir.score(exp,salary)
print('rmse',rmse)

print('r2 score,',r2_score)


