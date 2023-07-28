print("------String Operations------")
data=input("Enter a string: ")
length=len(data)
if length>=3:
    if data.endswith("ing"):
        data=data.rstrip("ing");
        data+='ly'+" <= Given String endswith 'ing' so 'ly' is added"
    else:
        data+='ing'+" <= Given String doesn't endswith 'ing' so 'ing' is added"
else:
    print("string has less than 3 characters")
print(data)

