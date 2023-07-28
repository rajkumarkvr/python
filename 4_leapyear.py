print("To check leap year or not")
year=int(input("Enter a year: "))
if year%4==0 and year%100!=0 or year%400==0:
    print("given year is leap year")
else:
    print("given year is not a leap year")
