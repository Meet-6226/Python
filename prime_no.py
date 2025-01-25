#Write a function that determines whether a number is prime.

num=int(input("Enter a number to check prime or not"))
for i in range(2,(num+1)//2):
    if num%i==0:
        print(num," is not a prime number")
        break
    else:
        print(num," is a prime number")