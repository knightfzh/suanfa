def quick_sort(s,low,high):
    i=low
    j=high
    if(low<high):
        temp=s[i]
        while(i<j):
            while(i<j and s[j]>=temp):
                j-=1
            if(i<j):
                s[i]=s[j]
                i+=1
            while(i<j and s[i]<temp):
                i+=1
            if(i<j):
                s[j]=s[i]
                j-=1

        s[i]=temp
        quick_sort(s,low,i-1)
        quick_sort(s,i+1,high)
   
s=[6,3,1,6,8,3,9]
quick_sort(s,0,len(s)-1)
print(s)
            
