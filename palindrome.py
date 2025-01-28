#Write a program that checks if a number is a palindrome

num=int(input("Enter a number to check for palindrome"))
pal=str(num)
if pal==pal[::-1]:
    print(num," is a palindrome")
else:
    print(num," is not a palindrome")