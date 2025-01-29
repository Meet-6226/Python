#Write a program that prints numbers from 1 to 10, but skip multiples of 3 using continue, and stop completely 
#if the number is 9 using break.

for num in range(1, 11):
    if num % 3 == 0:
        continue
    if num == 9:
        break
    print(num) 