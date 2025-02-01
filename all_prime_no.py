#Write a program that generates all prime numbers in a given range [start, end].

start=int(input("Enter a first number"))
last=int(input("Enter a last number"))
print(f"Prime numbers between {start} and {last} are ")
for num in range(start,last+1):
    for i in range(2,int(num**0.5) + 1):
        if num%i==0:
            break
    else:
        print(num)