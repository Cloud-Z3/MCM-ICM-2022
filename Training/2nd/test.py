from numpy import linalg
a=[3.9,3.33,4.27]
s=sum(a)
mina=min(a)
maxa=max(a)
a=[(ai-mina)/(maxa-mina) for ai in a]

matrix=[[1,3,1/2,2],[1/3,1,1/7,1/2],[2,7,1,4],[1/2,2,1/4,1]]

# matrix=[[1,1/2,4,3,3],[2,1,7,5,5],[1/4,1/7,1,1/2,1/3],[1/3,1/5,2,1,1],[1/3,1/5,3,1,1]]
# print(linalg.inv(matrix))
print(linalg.eigvals(matrix))
print(linalg.eig(matrix))
b=[-4.19535618e-01,-1.25301263e-01,-8.70335725e-01,-2.25400054e-01]
print(b)
sb=sum(b)
b=[ai/sb for ai in b]
print(b)
print(sum([0.2557,0.0764,0.5305,0.1374]))
