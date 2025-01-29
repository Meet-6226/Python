#Write a program to print a left-aligned triangle of stars of height n.

height=int(input("Enter a height of the triangle"))
for i in range(1,height+1):
    print("*"*i)