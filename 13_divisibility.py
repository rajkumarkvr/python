print("Diplay divisibility of numbers with in a range")

def divisible(lower,upper):
    for i in range(lower,upper+1):
        if i%3==0 and i%5!=0:
            print(i,end=" ")
lower=int(input("Enter the starting  number:"))
upper=int(input("Enter the ending    number:"))
divisible(lower,upper)
            
