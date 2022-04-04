from numpy import linalg

# matrix=[[1,3,1/2,2],[1/3,1,1/7,1/2],[2,7,1,4],[1/2,2,1/4,1]]
matrix=[
    [1,1/3,1/2,1/2,3,2],
    [3,1,2,1,9,5],
    [2,1/2,1,1/2,5,3],
    [2,1,2,1,7,4],
    [1/3,1/9,1/5,1/7,1,1/2],
    [1/2,1/5,1/3,1/4,2,1]
]
print(linalg.eigvals(matrix))
eigval,eigvec=linalg.eig(matrix)
print(eigval)
print(eigvec)
ans=[abs(e[0]) for e in eigvec]
s=sum(ans)
print([e/s for e in ans])
print(sum([0.1142,0.3236,0.1796,0.2820,0.0362,0.0644]))
print(sum([0.2357,0.6675,0.3704,0.5818,0.0746,0.1328]))