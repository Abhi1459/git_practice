def min_array(a:list)->int:
    result=a[0]
    for num in range(1,len(a)-1):
        if a[num]<result:
           result=a[num]
        

    return result

print(min_array([1,4,5,6,3]))