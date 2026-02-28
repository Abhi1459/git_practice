def second_largest(a:list)->int:
    result=a[0]
    for num in range(1,len(a)):
        if a[num]>result:
            result=a[num]
    b=[num for num in a if num!=result]
    ans=b[0]
    for j in range(1,len(b)):
        if b[j]>ans:
            ans=b[j]
    return ans
print(second_largest([4,5,1,3,6]))