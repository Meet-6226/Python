#Write a Python program to find the sum of all natural numbers up to a given number n.

num=int(input("Enter a number for addition series"))
for i in range(1,num+1):
    sum=num*(num+1)/2
print(f"Sum of all natural nos. till {num} is {sum:.0f}")