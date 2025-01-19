#Write a Python program that takes three numbers and prints the largest and the smallest numbers.

num1=int(input("Enter 1st no.: "))
num2=int(input("Enter 2nd no.: "))
num3=int(input("Enter 3rd no.: "))

largest=max(num1,num2,num3)
smallest=min(num1,num2,num3)
print("Largest no. is ",largest)
print("Smallest no. is ",smallest)