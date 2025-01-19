#Write a Python program that prompts the user for two numbers and prints their sum, difference, product, and quotient.

num1=float(input("Enter 1st no.: "))
num2=float(input("Enter 2st no.: "))
print("num1=",num1,"\tnum2=",num2)
sum=num1+num2
print("Sum of 2 nos. ",sum)
diff=num1-num2
print("Difference of 2 nos. ",diff)

mult=num1*num2
print("Product of 2 nos. ",mult)
if num2==0:
    print("Deniminator should not be zero")
else:
    div=num1/num2
    print("Quotient: ",div)