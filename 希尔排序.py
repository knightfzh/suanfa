def shell_sort(s):
      gap=len(s)
      while(gap>0):
          for i in range(gap,len(s)):
              temp=s[i]
              j=i
              while(j>=gap and temp<s[j-gap]):
                  s[j]=s[j-gap]
                  j-=gap
              s[j]=temp
          gap=gap//2


s=[5,4,3,2,6,8,9,7]
shell_sort(s)
print(s)
