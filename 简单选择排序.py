def select_sort(s):
    for i in range(0,len(s)):
        flag=i
        for j in range(i+1,len(s)):
            if s[j]<s[flag]:
                flag=j
        temp=s[i]
        s[i]=s[flag]
        s[flag]=temp


s=[1,3,5,89,23,14]
select_sort(s)
print(s)
        
                
