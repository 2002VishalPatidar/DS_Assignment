def sum(arry):
    ans=[]
    sum=6
    for i in range(len(arry)):
     for j in range(1+i,len(arry)): 
      if arry[i]+arry[j] == sum:
        ans.append((arry[i],arry[j]))
    print(ans)

arry=[1,2,3,5,4,7,8,9]
sum(arry)