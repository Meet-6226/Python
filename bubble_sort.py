#Implement the bubble sort algorithm to sort a list in ascending order.

def bubble_sort(lst):
    n = len(lst)
    for i in range(n):
        for j in range(0, n-i-1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
    return lst

lst = list(map(int, input("Enter elements separated by spaces: ").split()))
sorted_list = bubble_sort(lst)
print(f"Sorted list in ascending order: {sorted_list}")