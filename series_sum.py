#Write a Python program to calculate the sum of the series 1 + 1/2 + 1/3 + … + 1/n using a for loop.

n=int(input("Enter no of terms in series"))
sum=0
for i in range(1,n+1):
    sum+=1/i
print(f"The sum of the series 1 + 1/2 + 1/3 + ... + 1/{n} is: {sum:.3f}")