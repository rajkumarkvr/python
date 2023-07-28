"""
def modify_immutable(x):
    x=x+1
    print("Inside function ",x,"ID is",id(x))
    
num=10
modify_immutable(num)
print("Outside function",num,"ID is",id(num))

def add():
    a=a+1
    return a+b
a=10
b=20
print(add())
"""
def add():
    a=a+1
    return a+b
#i removed a & b immutale object
print(add())

