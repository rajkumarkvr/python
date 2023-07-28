a=10
print("Before a value ",a,"ID",id(a))

def my_function():
    global b
    b=20
my_function()
print("after a value ",b,"ID",id(b))
