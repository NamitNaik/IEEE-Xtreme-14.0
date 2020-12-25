import numpy as np
a1=[-1,0,1]
a2=[-1,0,1]
T=int(input())
result=list()
for i in range(T):
    N=int(input())
    finallist=list()
    for j in range(N):
        entry=input()
        entrylist=entry.split()
        entrylist=list(map(float, entrylist))
        finallist.append(entrylist)
    
    wts=list()

    for k in finallist:
        for w1 in a1:
            for w2 in a2:
                if k[2]==1:
                    if (w1*k[0])+(w2*k[1])>=0:
                        wts.append(w1)
                        wts.append(w2)
                        
    s=0
    t=0
    for k in finallist:
        if k[2]==-1:
            s=s+1
            i=0
            c=0
            while i<len(wts):
                if (wts[i]*k[0])+(wts[i+1]*k[1])<=0:
                    c=c+1
                i=i+2    
            if c>0:
                t=t+1
    
    if s==t:
        result.append("YES")
    else:
        result.append("NO")
        
for i in result:
    print(i);