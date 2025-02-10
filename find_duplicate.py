#Given a list, write a Python function to find all duplicate elements.

def duplicate_ele(number):
    duplicate=[]
    for num in number:
        if number.count(num)>1 and num not in duplicate:
            duplicate.append(num)
    return duplicate

number =list(map(int, input("Enter numbers separated by spaces: ").split()))
print("Duplicates:",duplicate_ele(number))