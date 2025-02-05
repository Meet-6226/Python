#Implement a linear search to find a given element in a list. Return the index if found, or -1 otherwise.

def linear_search(lst, target):
    for index, element in enumerate(lst):
        if element == target:
            return index  
    return -1 

lst = list(map(int, input("Enter elements separated by spaces: ").split()))
target = int(input("Enter the element to search for: "))
result = linear_search(lst, target)

if result != -1:
    print(f"Element {target} found at index {result}.")
else:
    print(f"Element {target} not found in the list.")