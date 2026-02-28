def reverse_list(a:list)->list:
    left=0
    right=len(a)-1
    while left<right:
        a[left]=a[right]
        a[right]=a[left]
        left+=1
        right-=1
    return a
print(reverse_list([1,2,3,5,7,8,9]))