def shift(s,low,high):
    i=low
    j=i*2+1
    temp=s[i]
    while(j<=high):
        if(j<high and s[j]<s[j+1]):
            j+=1
        if temp<s[j]:
            s[i]=s[j]
            i=j
            j=i*2+1
        else:
            break
    s[i]=temp



def heap_sort(s):
    n=len(s)
    i=n//2-1
    while(i>=0):
        shift(s,i,n-1)
        i-=1
    for i in range(n-1,0,-1):
        temp=s[0]
        s[0]=s[i]
        s[i]=temp
        shift(s,0,i-1)

s=[4,7,5,6,1,8,9,0]
heap_sort(s)
print(s)
