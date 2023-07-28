start=int(input("Enter starting value: "))
end=int(input("Enter ending value: "))
print("The primenumbers are:")
for i in range(start,end+1):
    if i>1:
        count=0
        for j in range(start,end+1):
            if i%j==0:
                count+=1
        if count==2:
            print(i)  
        
        


