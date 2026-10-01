def merge(s,low,mid,high):
    L=[]
    R=[]
    n1=mid-low+1  
    n2=high-mid
    for i in range(0,n1):
        L.append(s[low+i])  
    for j in range(0,n2):
        R.append(s[mid+j+1]) 
    i=0
    j=0
    k=low
    while(i<n1 and j<n2):
        if(L[i]<=R[j]):
            s[k]=L[i]
            i+=1
        else:
            s[k]=R[j]
            j+=1
        k+=1
    while(i<n1):
        s[k]=L[i]
        k+=1
        i+=1
    while(j<n2):
        s[k]=R[j]
        k+=1
        j+=1


def merge_sort(s,low,high):
    if(low<high):
        mid=(low+high)//2
        merge_sort(s,low,mid)
        merge_sort(s,mid+1,high)
        merge(s,low,mid,high)

s=[9,8,7,6,5,4,3,2,1]
merge_sort(s,0,len(s)-1)
print(s)
