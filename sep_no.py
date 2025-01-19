#Write a Python program that asks the user to input a float number, then prints the integer part (truncate), 
# and the fraction part separately.

x=float(input("Enter a float no."))
integer=int(x)
num=x-integer
print("Integer:",integer)
print(f"Fraction part:{num:.5f}")