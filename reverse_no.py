#Write a program to reverse the digits of a given integer (e.g., 123 -> 321).

num=int(input("Enter a no. to reverse "))
reverse= int(str(num)[::-1])
print(f"Reversed number is {reverse}")