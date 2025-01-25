#Write a program to display the multiplication table of a given integer up to 10.

table=int(input("Enter a number for required table"))
for i in range(1,11):
    mult=table*i
    print(f"{table}*{i}={mult}")
