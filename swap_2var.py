#Write a Python program that swaps the values of two variables without using a temporary variable.

num1=int(input("Enter 1st no.: "))
num2=int(input("Enter 2st no.: "))
print("Number before swapping:\na=",num1,"\tb=",num2)
num1,num2=num2,num1
print("Number after swapping:\na=",num1,"\tb=",num2)