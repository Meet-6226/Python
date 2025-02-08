#Write a Python program that counts the number of times a given element appears in a list.

def count_occurrences(lst, element):
    return lst.count(element)
lst = list(map(int, input("Enter elements separated by spaces: ").split()))
element = int(input("Enter the element to count: "))
count = count_occurrences(lst, element)
print(f"The element {element} appears {count} times in the list.")
