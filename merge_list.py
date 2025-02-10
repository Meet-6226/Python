#Write a function that merges two sorted lists into one sorted list.

def merge_sorted_lists(lst1, lst2):
    i, j = 0, 0
    merged_list = []
    
    while i < len(lst1) and j < len(lst2):
        if lst1[i] < lst2[j]:
            merged_list.append(lst1[i])
            i += 1
        else:
            merged_list.append(lst2[j])
            j += 1
    
    while i < len(lst1):
        merged_list.append(lst1[i])
        i += 1

    while j < len(lst2):
        merged_list.append(lst2[j])
        j += 1
    return merged_list

lst1 = [1, 3, 5]
lst2 = [2, 4, 6]

merged_list = merge_sorted_lists(lst1, lst2)
print(f"Merged sorted list: {merged_list}")