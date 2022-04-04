def maturaty(people,technologies,processes)->float:

    return ...

def read(file1,file2,file3):
    people=[]
    technologies=[]
    processes=[]
    with open(file1) as f:
        while True:
            pt=f.readline()
            if pt=='':
                break
            else:
                p=[]
                pt=list(map(float,pt.split()))
                id1,id2=0,6
                while id2<len(pt):
                    p.append(pt[id1:id2+1])
                    id1+=7
                    id2+=7
                p.append(pt[-2])
                p.append(pt[-1])
                people.append(p)
    with open(file2) as f:
        while True:
            tt=f.readline()
            if tt=='':
                break
            else:
                tt=list(map(float,tt.split()))
                technologies.append(tt)
    with open(file3) as f:
        while True:
            pt=f.readline()
            if pt=='':
                break
            else:
                pt=list(map(float,pt.split()))
                processes.append(pt)
    return people,technologies,processes

people,technologies,processes=read('./p2/people.txt','./p2/technologies.txt','./p2/processes.txt')
print(people,technologies,processes)
print(maturaty(people,technologies,processes))
