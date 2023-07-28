print("Basic trim & slicing ")
s=input("Enter a string:")
print("First 2 characters are:",s[:2])
print("Last character of a string:",s[-1])
print("Reversed string is: ",s[::-1])
print("Incremented by one character:",s[::2])
print("With in a range: ",s[2:6])
s='\twelcome\t'
print(s,"all")
print(s.strip(),"all")
print(s.lstrip(),'all')
print(s.rstrip(),'all')
s='welcome'
print(s.strip('come'))
print(s.strip('we'))
print(s.lstrip('we'))
print(s.rstrip('we'))

