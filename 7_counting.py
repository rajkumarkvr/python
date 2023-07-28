data=input("Enter any paragraph: ").lower()
space_count=0
char_count=0
vowel_count=0
for ch in data:
    if ch>='a'and ch<='z':
        char_count+=1
    if ch==' ':
        space_count+=1
    if ch in ['a','e','i','o','u']:
        vowel_count+=1

print("Character count is: ",char_count)
print("Vowel count is: ",vowel_count)
print("White space count is: ",space_count)
