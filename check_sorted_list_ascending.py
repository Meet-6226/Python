#Write a Python function to check if a given list is sorted in ascending order.

number =list(map(int, input("Enter numbers separated by spaces: ").split()))
for i in range(len(number) - 1):
    if number[i] > number[i + 1]:
        print("The given list is not in ascending order")
        break
else:
    print("The given list is in ascending order")