# user_name=str(input("Enter a name"))
# user_age=int(input("Enter age"))
# print(F"{user_name} is {user_age} years old")

# age=int(input("Enter age:- "))
# print("Adult"if age<35 else "Old")

# a=["even" if i%2==0 else "odd" for i in range(0,13) ]

# print(a)
# double=lambda x:x*2
# print(double(23))
# random_list=[('Abhi',23),('rahul',12),("Kishan",45)]
# print(sorted(random_list,key=lambda x:x[1],reverse=True))

# a=[f'{i}{j}'for i in ["A","B","C","D","E"] for j in range(1,6)if f'{i}{j}'!="C3"]
 
# print(a)

a=[j for i in [[1,3,4,5,6],[1,3,4,5,6,9,7,9,78,3]] for j in i]
print(a)