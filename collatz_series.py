#Write a program that displays the Collatz sequence for any positive integer given by the user.

num=int(input("Enter the first number of Collatz series"))
print(f"Collatz sequence starting from {num}:")
while num!=1:
    print(num,end=", ")
    if num%2==0:
        num=num//2
    else:
        num=3*num+1
print(1)