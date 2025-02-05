#Write a program to reverse a list in-place (without using reversed() or slicing).

def reverse_list_in_place(lst):
    for i in range(len(lst) // 2):
        lst[i], lst[len(lst) - 1 - i] = lst[len(lst) - 1 - i], lst[i]

lst = list(map(int, input("Enter elements separated by spaces: ").split()))
reverse_list_in_place(lst)
print(f"Reversed list: {lst}")