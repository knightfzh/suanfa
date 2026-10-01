

def Prim(n,MGraph,v0)->int:
    vSet=[]
    lowCost=[]
  
    for i in range(0,n):
        lowCost.append(MGraph[0][i])
    for i in range(0,n):
        vSet.append(0)
    v=v0
    vSet[v]=1
    sum=0
    for i in range(0,n-1):
        min=255               #255代表无穷大
        for  j in range(0,n):
            if(lowCost[j]<min and vSet[j]==0):
                min=lowCost[j]
                k=j
        vSet[k]=1
        sum+=min
        v=k
        for j in range(0,n):
            if(lowCost[j]>MGraph[v][j] and vSet[j]==0):
                lowCost[j]=MGraph[v][j]
    return sum   
    
        
MGraph=[[255,1,2,3,255,255],[1,255,7,255,8,255],[2,7,255,6,4,255],[3,255,6,255,255,5],[255,8,4,255,255,9],[255,8,4,255,255,9]]
print(Prim(6,MGraph,0))
