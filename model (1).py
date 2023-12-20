# -*- coding: utf-8 -*-
"""
Created on Tue Aug 15 14:10:50 2023

@author: SRIRAM
"""

exp=(3,2,1,7,8,2,10,14,11)
salary=(30000,27000,25000,45000,46500,26000,47000,65000,50000)
x=exp
y=salary
xbr=0

#find xbr
for i in x:
    xbr=i+xbr
xbr=xbr/len(x)
#print(xbr)
#find ybr
ybr=0
for i in y:
    ybr=i+ybr
ybr=ybr/len(y)
#print(ybr)
xy_lst=[]
num=0
for i in range(len(salary)):
    num +=(x[i]-xbr)*(y[i]-ybr)
    xy_lst.append(num)
#print(num)
    
xlst=[]
for i in x:
   x=(i-xbr)**2
   xlst.append(x)
#print(xlst)
num2=0
for i in xlst:
    num2=i+num2
#print(num2)
m=num/num2
c=ybr-m*xbr
final_ans=[]
for i in exp:
    y=m*i+c
    final_ans.append(y)
#print('final Y:',final_ans)
x1=int(input('enter the years of experience = '))
y=m*x1+c
print(x1,'years of experience will get the pay of' ,y)

    

    