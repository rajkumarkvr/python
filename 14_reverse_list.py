numbersList=[]
print("-----Display a list in reverse order---")
totalNumCount=int(input("Enter the number of elements in list: "))
print("Enter the numbers :")
for i in range(totalNumCount):
    numbersList.append(int(input()))
print("The numbers in the list before reversed order ",numbersList)
numbersList.reverse()
print("The numbers in the list after reversed order ",numbersList)


