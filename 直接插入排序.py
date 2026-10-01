def insert_sort(s):
    for i in range(1,len(s)):
        temp=s[i]              #temp为待排关键字
        j=i-1                  #s[0]到s[j]为已排关键字
        while(j>=0 and temp<s[j]):
            s[j+1]=s[j]        #大于temp的已排关键字整体后移
            j-=1
        s[j+1]=temp            #待排关键字插入





#########主程序测试insert_sort()函数###########
s=[7,6,5,4,3,8,7]            
insert_sort(s)
print(s)
        
