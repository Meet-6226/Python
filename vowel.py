#Write a program that counts the number of vowels in a string.

string=str(input("Enter a string"))
vowel="AaEeIiOoUu"
count=0
for char in string:
    if char in vowel:
        count+=1
print(f"The number of vowels in the string is: {count}")