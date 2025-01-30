#Write a Python function to compute the LCM (Least Common Multiple) of two numbers, leveraging the GCD.

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
a,b=num1,num2
while b!=0:
    a,b=b,a%b
gcd=a
lcm=(num1*num2)//gcd
print(f"The LCM of {num1} and {num2} is {lcm}.")