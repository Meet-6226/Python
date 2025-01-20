#Write a program that checks if a given year is a leap year.
yr=int(input("Enter aa year to check for leap year"))
if yr%4==0:
    print(yr," is a leap year")
else:
    print(yr," is not a leap year")