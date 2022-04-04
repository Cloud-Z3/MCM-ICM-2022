# 梯度下降
# 求y最小值
# 3个x均小于1大于0
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
sns.set(style="white", palette="muted", color_codes=True)
# plt.rc('text',usetex=True)
plt.rc('font', family='serif')

def f(x1,x2,x3):
    return -(-0.057887797815248235*x1+0.1758891724397263*x2+0.11620566483160263*x3+0.18461542159090832*x1*x2+0.0907466317177971*x1*x3+0.24355665831425927*x2*x3+0.2468742489209547*x1*x2*x3)
# y=(-0.057887797815248235*x1+0.1758891724397263*x2+0.11620566483160263*x3+0.18461542159090832*x1*x2+0.0907466317177971*x1*x3+0.24355665831425927*x2*x3+0.2468742489209547*x1*x2*x3)
def df1(x1,x2,x3):
    return 0.057887797815248235-0.18461542159090832*x2-0.0907466317177971*x3-0.2468742489209547*x2*x3

def df2(x1,x2,x3):
    return -0.1758891724397263-0.18461542159090832*x1-0.24355665831425927*x3-0.2468742489209547*x1*x3

def df3(x1,x2,x3):
    return -0.11620566483160263-0.0907466317177971*x1-0.24355665831425927*x2-0.2468742489209547*x1*x2

# alpha=0.0001
# ans1=[]
#
# # 第731天的x作为初始点
# flag1=0
# flag2=0
#
# GD_X = [] #每次x更新后把值存在这个列表里面
# GD_Y = [] #每次更新x后目标函数的值存在这个列表里面
#
# #seed=9
# # x1=0.6771531038888514
# # x2=0.6843912398353547
# # x3=0.6894732795486307
#
# #seed=10
# x1=0.6772315799900468
# x2=0.6503411731864872
# x3=0.35459014706102954
#
# #随机初始化的x,其他的值也可以
# f_current = f(x1,x2,x3)
# iter_num = 0
# f_change=-1
# ans=[]
# x10=-1
# x20=-1
# x30=-1
# eps=1e-10     # 误差很小很小
# num1=100000
# x=[]
# y=[]
# z=[]
# while iter_num <num1 and abs(f_change) > eps and x1>=0 and x1<=1 and x2>=0 and x2<=1 and x3>=0 and x3<=1: #迭代次数小于100次或者函数变化小于1e-10次方时停止迭代
#         x10 = x1
#         x20 = x2
#         x30 = x3
#         iter_num += 1
#         x1 = x1 - alpha * df1(x10,x20,x30)
#         x2 = x2 - alpha * df2(x10, x20, x30)
#         x3 = x3 - alpha * df3(x10, x20, x30)
#         tmp = f(x1,x2,x3)
#         f_change = abs(f_current - tmp)
#         f_current = tmp
#         GD_X.append([x1,x2,x3])
#         GD_Y.append(f_current)
#         if iter_num==num1:
#             flag1=1
#         if abs(f_change)<=eps:
#             flag2=1
#         x.append(x1)
#         y.append(x2)
#         z.append(x3)
        
# print("最终误差：",f_change)
# print("迭代次数：",iter_num)
# print("{:.10f}".format(GD_Y[-1]))  # 无限接近0
# if x1>=0 and x1<=1 and x2>=0 and x2<=1 and x3>=0 and x3<=1:
#     ans1.append([x1,x2,x3,GD_Y[-1]])
# print(x1)
# print(x2)
# print(x3)
# print(x10)
# print(x20)
# print(x30)
# print(GD_Y)
# ans1.append([x10, x20, x30, GD_Y[-1]])
# print("y的最大值：",-ans1[0][-1],"x的值:",ans1[0][0:3])
# if flag1==1:
#     print("迭代次数不够")
# if flag2==1:
#     print("出现误差允许范围内的极值点")
# if flag2==0 and flag1==0:
#     print("极值点出现在边界")
# print(GD_Y)

def Singleplot(x,y,z,name):

    ax = plt.subplot(111, projection='3d')

    ax.plot(x, y, z,)
    ax.set_xlabel('$x_1$')
    ax.set_ylabel('$x_2$')
    ax.set_zlabel('$x_3$')
    # plt.savefig('./image/' + name + '.png', dpi=1000)
    plt.show()

def plot1(GD_Y,name):
    data1=[]
    for i in range(len(GD_Y)):
        data1.append([i,-GD_Y[i]])
    data2=pd.DataFrame(data=data1,columns=['$t$','$M$'])
    sns.lineplot(data=data2,x='$t$',y='$M$')
    plt.savefig('./image/' + name + '.png', dpi=1000)
    plt.show()

# Singleplot(x,y,z)
# plot1(GD_Y)
'''
seed=10
最终误差： 9.636641309651583e-05
迭代次数： 6521
y的最大值： 0.7334084602169638 x的值: [0.8376403542093563, 0.9999553798481033, 0.7023383907724895]
极值点在边界
'''

