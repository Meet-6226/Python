#Write a function that returns the largest and the smallest elements in a given list.

def large_small(num):
    smallest = largest = num[0]

    for i in num:
        if i < smallest:
            smallest = i
        if i > largest:
            largest = i
    return largest, smallest

num= list(map(int, input("Enter numbers separated by spaces: ").split()))
largest,smallest=large_small(num)
print(f"The largest element is: {largest}")
print(f"The smallest element is: {smallest}")