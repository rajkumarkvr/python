numbers=(1,2,3,4,5,6,7,8,9,10,1)
#Expected output
#12345
#678910
mid=int(len(numbers)/2)
"""
for i in range(len(numbers)):
    if i==mid:
        print()
    print(numbers[i],end=" ")
"""
print("First Half Values:",numbers[0:mid])
print("Next Half Values:",numbers[mid:])
