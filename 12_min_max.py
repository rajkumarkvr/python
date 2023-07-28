numbersList=[]
print("Find minimum & Maximum value in a list")
totalNumCount=int(input("Enter the number of elements in list: "))
print("Enter the numbers :")
for i in range(totalNumCount):
    numbersList.append(int(input()))
print("The numbers inside the list",numbersList)
print("The smallest element in this list: ",min(numbersList))
print("The largest  element in this list: ",max(numbersList))

