# -*- coding: utf-8 -*-
"""
Created on Sat Nov 11 15:27:11 2017

@author: ljw11554
"""
# rescale data to 0-1 values to "normalize" for SOM
import pandas as pd
import numpy as N
import math

inputdf = pd.read_csv("G:\\informatics\\merra2_phl_metvars.csv")

date_array = N.array(inputdf['Dates'])
h500_array = N.array(inputdf['h500'])
slp_array = N.array(inputdf['slp'])
h850_array = N.array(inputdf['h850'])
q850_array = N.array(inputdf['q850'])
qv10m_array = N.array(inputdf['qv10m'])
t2m_array = N.array(inputdf['t2m'])
t2mdew_array = N.array(inputdf['t2mdew'])
tqv_array = N.array(inputdf['tqv'])
u850_array = N.array(inputdf['u850'])
v850_array = N.array(inputdf['v850'])
u10m_array = N.array(inputdf['u10m'])
v10m_array = N.array(inputdf['v10m'])


h500_norm = []
xmin = N.min(h500_array)
xmax = N.max(h500_array)
for x in N.arange(0,len(h500_array)):
    xi = h500_array[x]
    xnew = (xi - xmin)/(xmax - xmin)
    h500_norm.append(xnew)
    del xi, xnew    
h500_norm_array = N.array(h500_norm)

slp_norm = []
xmin = N.min(slp_array)
xmax = N.max(slp_array)
for x in N.arange(0,len(slp_array)):
    xi = slp_array[x]
    xnew = (xi - xmin)/(xmax - xmin)
    slp_norm.append(xnew)
    del xi, xnew    
slp_norm_array = N.array(slp_norm)

h850_norm = []
xmin = N.min(h850_array)
xmax = N.max(h850_array)
for x in N.arange(0,len(h850_array)):
    xi = h850_array[x]
    xnew = (xi - xmin)/(xmax - xmin)
    h850_norm.append(xnew)
    del xi, xnew    
h850_norm_array = N.array(h850_norm)

q850_norm = []
xmin = N.min(q850_array)
xmax = N.max(q850_array)
for x in N.arange(0,len(q850_array)):
    xi = q850_array[x]
    xnew = (xi - xmin)/(xmax - xmin)
    q850_norm.append(xnew)
    del xi, xnew    
q850_norm_array = N.array(q850_norm)

qv10m_norm = []
xmin = N.min(qv10m_array)
xmax = N.max(qv10m_array)
for x in N.arange(0,len(qv10m_array)):
    xi = qv10m_array[x]
    xnew = (xi - xmin)/(xmax - xmin)
    qv10m_norm.append(xnew)
    del xi, xnew    
qv10m_norm_array = N.array(qv10m_norm)

t2m_norm = []
xmin = N.min(t2m_array)
xmax = N.max(t2m_array)
for x in N.arange(0,len(t2m_array)):
    xi = t2m_array[x]
    xnew = (xi - xmin)/(xmax - xmin)
    t2m_norm.append(xnew)
    del xi, xnew    
t2m_norm_array = N.array(t2m_norm)

t2mdew_norm = []
xmin = N.min(t2mdew_array)
xmax = N.max(t2mdew_array)
for x in N.arange(0,len(t2mdew_array)):
    xi = t2mdew_array[x]
    xnew = (xi - xmin)/(xmax - xmin)
    t2mdew_norm.append(xnew)
    del xi, xnew    
t2mdew_norm_array = N.array(t2mdew_norm)

tqv_norm = []
xmin = N.min(tqv_array)
xmax = N.max(tqv_array)
for x in N.arange(0,len(tqv_array)):
    xi = tqv_array[x]
    xnew = (xi - xmin)/(xmax - xmin)
    tqv_norm.append(xnew)
    del xi, xnew    
tqv_norm_array = N.array(tqv_norm)

u850_norm = []
xmin = N.min(u850_array)
xmax = N.max(u850_array)
for x in N.arange(0,len(u850_array)):
    xi = u850_array[x]
    xnew = (xi - xmin)/(xmax - xmin)
    u850_norm.append(xnew)
    del xi, xnew    
u850_norm_array = N.array(u850_norm)

v850_norm = []
xmin = N.min(v850_array)
xmax = N.max(v850_array)
for x in N.arange(0,len(v850_array)):
    xi = v850_array[x]
    xnew = (xi - xmin)/(xmax - xmin)
    v850_norm.append(xnew)
    del xi, xnew    
v850_norm_array = N.array(v850_norm)

u10m_norm = []
xmin = N.min(u10m_array)
xmax = N.max(u10m_array)
for x in N.arange(0,len(u10m_array)):
    xi = u10m_array[x]
    xnew = (xi - xmin)/(xmax - xmin)
    u10m_norm.append(xnew)
    del xi, xnew    
u10m_norm_array = N.array(u10m_norm)

v10m_norm = []
xmin = N.min(v10m_array)
xmax = N.max(v10m_array)
for x in N.arange(0,len(v10m_array)):
    xi = v10m_array[x]
    xnew = (xi - xmin)/(xmax - xmin)
    v10m_norm.append(xnew)
    del xi, xnew    
v10m_norm_array = N.array(v10m_norm)

df1 = pd.DataFrame(date_array,columns=['Dates'])
df2 = pd.DataFrame(h500_norm_array,columns=['h500'])  
df3 = pd.DataFrame(slp_norm_array,columns=['slp'])
df4 = pd.DataFrame(h850_norm_array,columns=['h850'])
df5 = pd.DataFrame(q850_norm_array,columns=['q850'])
df6 = pd.DataFrame(qv10m_norm_array,columns=['qv10m'])
df7 = pd.DataFrame(t2m_norm_array,columns=['t2m'])
df8 = pd.DataFrame(t2mdew_norm_array,columns=['t2mdew'])
df9 = pd.DataFrame(tqv_norm_array,columns=['tqv'])
df10 = pd.DataFrame(u850_norm_array,columns=['u850'])
df11 = pd.DataFrame(v850_norm_array,columns=['v850'])
df12 = pd.DataFrame(u10m_norm_array,columns=['u10m'])
df13 = pd.DataFrame(v10m_norm_array,columns=['v10m'])

new_df = pd.concat([df1,df2,df3,df4,df5,df6,df7,df8,df9,df10,df11,df12,df13],join='outer',axis=1)
new_df.to_csv("G:\\informatics\\merra2_phl_metvars_normalized_withDate.csv")