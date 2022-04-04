import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

def snsplot(DF:pd.DataFrame,name,idx='index')->None:
    column=DF.columns
    index=DF.index
    matrix=[]
    for col in column:
        for idx in index:
            matrix.append([idx,DF[col][idx],col])
    data=pd.DataFrame(data=matrix,columns=['time','value',''])
    fig=plt.figure(figsize=(8,5))
    fig.legend(loc='upper right',labels=column)
    sns.lineplot(data=data,x='time',y='value',hue='')
    # plt.savefig('./image/'+name+'.png',dpi=1000)
    plt.show()


def list2str(a):
    return ' '.join([list2str(ai) if type(ai)==list else str(ai) for ai in a])

if __name__=='__main__':
    print(list2str([[1,2,[7,8,9]],1,2,3,5,6]))
    snsplot(pd.DataFrame([1, 2, 3], [4, 5, 6]), '张三','')