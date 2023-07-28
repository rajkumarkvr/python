p=2

while p*p<=100:
        print("p=",p)
        for i in range(p*p,100+1,p):
            print(i)
        p+=1
