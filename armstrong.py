#Write a function to check if a 3-digit number is an Armstrong number (e.g., 153 -> 1^3 + 5^3 + 3^3 = 153).

num=int(input("Enter a 3 digit number to check for armstrong"))

digit1=num//100
digit2=(num//10)%10
digit3=num%10
armstrong=digit1**3+digit2**3+digit3**3

if armstrong==num:
    print(f"{num} is a armstrong number")
else:
    print(f"{num} is not a armstrong number")