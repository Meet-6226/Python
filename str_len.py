#Write a Python function that takes a string and returns its length without using the built-in len() function.

str=input("Enter a string: ")
count=0
for char in str:
    count+=1
print("The length of the string is: ",count)
