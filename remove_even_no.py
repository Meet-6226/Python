#Write a program to remove all even numbers from a list of integers.

number =list(map(int, input("Enter numbers separated by spaces: ").split()))
print("List with no even numbers:", [num for num in number if num % 2 != 0])