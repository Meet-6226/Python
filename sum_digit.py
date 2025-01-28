#Write a program that calculates the sum of digits of a given integer.

number=int(input("Enter an integer to calculate the sum of its digits: "))
num=number
sum=0
while num>0:
    sum+=(num%10)
    num=num//10
print(f"The sum of digits of {number} is {sum}")