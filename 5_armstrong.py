print("Armstrong numbers between range.")
lower=int(input("Enter lower limit: "))
upper=int(input("Enter upper limit: "))
print("The armstrong numbers are:")
for num in range(lower,upper+1):
    if num>1:
        sum=0  
        temp=num
        while temp!=0:
            sum+=(temp%10)**3
            temp//=10
        if num==sum:
            print(num)

