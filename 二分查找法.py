def binary_search(s,low,high,key)->int:
    while(low<=high):
        mid=(low+high)//2 
        if(s[mid]==key):
            return mid
        elif s[mid]>key:
            high=mid-1
        else:
            low=mid+1
    return -1

#####主程序测试binary_serach()函数#####
s=[0,1,2,3,4,5,6,7,8,9]
print(binary_search(s,0,len(s),3))



    
