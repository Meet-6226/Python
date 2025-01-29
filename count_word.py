#Write a program to count the number of words in a user-input string (words are separated by spaces).

string=str(input("Enter a string to check nof words"))
space=' '
count=1
for char in string:
    if char==space:
        count+=1
print(f"There are {count} words in the string")