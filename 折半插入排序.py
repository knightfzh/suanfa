def binary_insert_sort(s):
    for i in range(1,len(s)):
        temp=s[i]
        low=0
        high=i-1
        while(low<=high):
            mid=(low+high)//2
            if (s[mid]==temp):
                break
            elif s[mid]<temp:
                low=mid+1
            else:
                high=mid-1
        j=i-1
        while(j>=high+1):
            s[j+1]=s[j]
            j-=1
        s[high+1]=temp


s=[2,5,7,9,34,67,4]
binary_insert_sort(s)
print(s)

