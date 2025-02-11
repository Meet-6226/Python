#Write a program to shuffle a list in-place (you can use random.shuffle or implement your own shuffling algorithm).

import random
numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
random.shuffle(numbers)

print("Shuffled list:", numbers)