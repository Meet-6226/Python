#Given two lists of same length, create a dictionary mapping elements of one list to corresponding elements of the other

keys = ['a', 'b', 'c']
values = [1, 2, 3]

dictionary = dict(zip(keys, values))
print(dictionary)