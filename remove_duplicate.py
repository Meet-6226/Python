#Write a Python function that removes duplicate elements from a list and returns the new list.

def remove_dupli(detail):
    element=[]
    for item in detail:
        if item not in element:
            element.append(item)
    return element

detail= list(input("Enter elements separated by spaces: ").split())
result=remove_dupli(detail)
print(f"List after removing duplicates: {result}")