# def print_X_time(parameters="rahul",loop=5):
#     counter=0
#     while counter<loop:
#         print("ALL Good",parameters)
#         counter+=1
#     return "loop is finished"
# test=print_X_time(loop=3)
# print(test)

# def shouter(a:str,b:int)->str:
#     for _ in range(b):
#         print(a.upper())

# shouter("real",3)

def shout(string_req,req=7):
    if req<9:
        print((string_req+"\n")*req)
    else:
        print('you are too loud')
    return 'done'
test=shout("Rahul")

print(test)
