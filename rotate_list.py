#Write a function to rotate a list by k positions to the right.For instance [1,2,3,4,5] rotated by 2 becomes [4,5,1,2,3]

def rotate_list(lst, k):
    k = k % len(lst)
    return lst[-k:] + lst[:-k]

lst = list(map(int, input("Enter elements separated by spaces: ").split()))
k = int(input("Enter the number of positions to rotate: "))
rotated_lst = rotate_list(lst, k)
print(f"List after rotation: {rotated_lst}")