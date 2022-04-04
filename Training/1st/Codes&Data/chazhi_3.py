# -*-coding:utf-8 -*-
from scipy import interpolate
import pylab as pl
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df_ap=pd.read_csv('.\\2020_Problem_D_DATA\\Flow Centrality_ave.csv')
print(df_ap)
print(np.array(list(df_ap['TimeSpan'])))

# x=np.linspace(0,10,11)
# #x=[  0.   1.   2.   3.   4.   5.   6.   7.   8.   9.  10.]

x=np.array(list(map(float,df_ap['TimeSpan'])))

print(type(x))
y=np.array(list(map(float,df_ap['Flow Centrality'])))
# y=np.sin(x)
print(x)
print(y)
xnew=np.linspace(x[0],x[-1],500)
print(xnew)
# pl.plot(x,y,"ro")

for kind in ["quadratic"]:#插值方式
    #"nearest","zero"为阶梯插值
    #slinear 线性插值
    #"quadratic","cubic" 为2阶、3阶B样条曲线插值
    f=interpolate.interp1d(x,y,kind=kind)
    # ‘slinear’, ‘quadratic’ and ‘cubic’ refer to a spline interpolation of first, second or third order)
    ynew=f(xnew)
    plt.xlabel("TimeSpan")
    plt.ylabel("Flow Centrality")
    pl.plot(xnew,ynew)
    plt.savefig('.\\2020_Problem_D_DATA\\拟合曲线\\Flow Centrality_ave.png',dpi=600)
pl.show()