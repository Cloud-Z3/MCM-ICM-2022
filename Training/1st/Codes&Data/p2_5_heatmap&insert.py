import numpy as np
import pandas as pd
from scipy.interpolate import interp2d
from matplotlib import pyplot as plt
file1='2020_Problem_D_DATA'
file2='2020_Problem_D_DATA_After_Pro'
file3='Image'
file='passingevents_match1.csv'
p1='Problem1'
p2='Problem2'
p3='Problem3'
p4='Problem4'
'''
data1 = pd.read_csv('data1.csv')
data2 = pd.read_csv('data2.csv')
data3 = pd.read_csv('data3.csv')
data4 = pd.read_csv('data4.csv')
data = [data1, data2, data3, data4]'''
data=pd.read_csv(file2+'/'+p2+'/MatchData.csv')
data['Goal Difference']=data['OwnScore']-data['OpponentScore']
columns=['Goal Difference','Flow Centrality','Team PlayeRank','MaxEigenvalue','Connectivity','Clustering Coefficient','Shortest-path Length']
corr=data[columns]

def plot_weather_heatmap(dataList, title):
    plt.figure(figsize=(25, 25))
    for i in range(len(dataList)):
        data = dataList[i]
        '''
        方法一：从csv文件中读取数据
        '''

        # pos = np.array(data['pos']/180*np.pi)
        # ind = np.array(data.columns[1:], dtype=np.int)
        # values = np.array(data[ind.astype('str')])

        '''
        方法二：随机产生数据
        '''
        pos = np.radians(np.linspace(0, 360, 30))
        ind = np.arange(0, 90, 10)
        values = np.random.random((pos.size, ind.size))

        # 计算插值函数
        func = interp2d(pos, ind, values.T, kind='cubic')
        tnew = np.linspace(0, 2 * np.pi, 200)  # theta
        # 绘图数据点
        rnew = np.linspace(0, 90, 100)  # r
        vnew = func(tnew, rnew)
        tnew, rnew = np.meshgrid(tnew, rnew)
        ax = plt.subplot(2, 2, i + 1, projection='polar')
        plt.pcolor(tnew, rnew, vnew, cmap='jet')
        plt.grid(c='black')
        plt.colorbar()
        ax.set_theta_zero_location("N")
        ax.set_theta_direction(-1)
        plt.title(title[i], fontsize=20)
        # 设置坐标标签标注和字体大小
        plt.xlabel(' ', fontsize=15)
        plt.ylabel(' ', fontsize=15)

        # 设置坐标刻度字体大小
        plt.xticks(fontsize=15, rotation=90)
        plt.yticks(fontsize=15)
        # cb.set_label("Pixel reflectance")


title = ['Goal Difference','Flow Centrality','Team PlayeRank','MaxEigenvalue','Connectivity','Clustering Coefficient','Shortest-path Length']
plot_weather_heatmap(corr, title)
#plt.savefig("pic.png", dpi=300)
plt.show()

