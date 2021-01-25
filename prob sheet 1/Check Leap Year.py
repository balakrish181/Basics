year=int(input("Enter a year to check for leap year:"))
if(((year%4==0)and(year%100!=0))or(year%400==0)):
    print("{} is a leap year".format(year))
else:
    print("{} is not a leap year".format(year))
