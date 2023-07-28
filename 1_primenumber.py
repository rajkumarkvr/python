#write a program to check if a number is prime or not
fact=0
number=int(input('Enter a number: '))
for divisor in range(1,number+1):
    print(divisor)
    if number%divisor==0:
        fact+=1
        
if fact==2:
    print(number,"is prime.")
else:
    print(number,"is not prime.")
