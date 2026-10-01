def bubble_sort(s):
    for i in range(0,len(s)-1):
        flag=0
        for j in range(0,len(s)-i-1):
            if s[j]>s[j+1]:
                temp=s[j]
                s[j]=s[j+1]
                s[j+1]=temp
                flag=1
        if flag==0:
            break

s=[53,67,89,34,12,78,23,67]
bubble_sort(s)
print(s)
