#Implement the Euclidean algorithm to find the GCD (Greatest Common Divisor) of two numbers using a while loop.

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
a,b=num1,num2
while b!=0:
    temp=a%b
    a=b
    b=temp
print(f"The GCD of {num1} and {num2} is {a}.")