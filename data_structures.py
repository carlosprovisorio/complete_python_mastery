# lists
# letters = ["a", "b", "c"]  # list
# matrix = [[0, 1], [2, 3]]  # two dimensional list
# zeros = [0] * 5
# combined = zeros + letters
# numbers = list(range(20))
# chars = list("Hello World")
# print(chars)
# print(len(chars))


# Accessing items
# letters = ["a", "b", "c", "d"]
# letters[0] = "A"
# print(letters[0:3])
# print(letters[::2])


# numbers = list(range(20))
# print(numbers[::-1])
# print(numbers[::2])


# List Unpacking
# numbers = [1, 2, 3]
# first, second, third = numbers
# print(first, second, third)

# numbers = [1, 2, 3, 4, 4, 4, 4, 4, 9]
# # first, second, *other = numbers
# first, *other, last = numbers
# print(first, last)
# print(other)

# Looping over lists
# letters = ["a", "b", "c"]
# for letter in enumerate(letters):
#     print(letter[0], letter[1])

# using the unpacking approach
# letters = ["a", "b", "c"]
# for index, letter in enumerate(letters):
#     print(index, letter)


# adding or removing items

# letters = ["a", "b", "c"]

# # Add
# letters.append("d")
# letters.insert(0, "_")

# # Remove
# letters.pop(0)
# letters.remove("b")
# del letters[0:3]
# letters.clear()
# print(letters)


# Finding Items

# letters = ["a", "b", "c"]

# print(letters.count("d"))
# if "d" in letters:
#     print(letters.index("d"))

# Sorting lists

# numbers = [3, 51, 2, 8, 9]
# # numbers.sort()  # Ascending order
# # numbers.sort(reverse=True)  # Descending order
# print(sorted(numbers))  # It sort a new list without modifying the initial list
# print(
#     sorted(numbers, reverse=True)
# )  # It sort a new list without modifying the initial list
# print(numbers)  # original list

# sorting a tuple
# items = [
#     ("Product", 10),
#     ("Product", 9),
#     ("Product", 12),
# ]


# def sorting_item(item):
#     return item[1]


# items.sort(key=sorting_item)
# print(items)


# lambda function - Better option than the above
# it's a one line anonimous function

# items.sort(key=lambda item: item[1])
# print(items)

# Map Function
# items = [
#     ("Product", 10),
#     ("Product", 9),
#     ("Product", 12),
# ]

# prices = []
# for item in items:
#     prices.append(item[1])

# Instead use Map function
# prices = list(map(lambda item: item[1], items))
# print(prices)

# Fibonscci Sequence


# This approach uses a simple iterative method which is easy to understand and implement.
# def fibonacci_junior(n):
#     if n <= 0:
#         return []
#     elif n == 1:
#         return [0]

#     sequence = [0, 1]
#     for i in range(2, n):
#         sequence.append(sequence[-1] + sequence[-2])
#     return sequence


# print(fibonacci_junior(10))


# # This approach uses a recursive method with memoization to improve efficiency.
# def fibonacci_intermediate(n, memo=None):
#     if memo is None:
#         memo = {}
#     if n in memo:
#         return memo[n]
#     if n <= 0:
#         return []
#     if n == 1:
#         return [0]
#     if n == 2:
#         return [0, 1]

#     memo[n] = fibonacci_intermediate(n - 1, memo) + [
#         fibonacci_intermediate(n - 1, memo)[-1]
#         + fibonacci_intermediate(n - 2, memo)[-1]
#     ]
#     return memo[n]


# print(fibonacci_intermediate(10))


# This approach uses a generator for better memory efficiency,
# especially useful for generating large sequences.


# def fibonacci_advanced(n):
#     def generator():
#         a, b = 0, 1
#         for _ in range(n):
#             yield a
#             a, b = b, a + b

#     return list(generator())


# print(fibonacci_advanced(10))


# Filter function

# items = [
#     ("Product1", 10),
#     ("Product2", 9),
#     ("Product3", 12),
# ]

# filtered = list(filter(lambda item: item[1] >= 10, items))
# print(filtered)

# List comprehensions

# items = [
#     ("Product1", 10),
#     ("Product2", 9),
#     ("Product3", 12),
# ]

# prices = list(map(lambda item: item[1], items))  # mappin
# prices = [item[1] for item in items]  # alternative more readabl
# filtered = list(filter(lambda item: item[1] >= 10, items))
# filtered = [item for item in items if item[1] >= 10]


# zip Function
# combine multiple lists

# list1 = [1, 2, 3]
# list2 = [10, 20, 30]

# print(list(zip(list1, list2)))

# # Stacks
# LIFO - LAst In First Out

# browsing_session = []
# browsing_session.append(1)
# browsing_session.pop()
# if not browsing_session:
#     browsing_session


# Queues
# FIFO - First In First Out

# from collections import deque

# queue = deque([])
# queue.append(1)
# queue.append(2)
# queue.append(3)
# queue.popleft()
# print(queue)
# if not queue:
#     print("empty")


# Tuples = Read only list immutable
# we can't add or remove to the list

# point = (1, 2)
# point2 = (1,)
# point3 = ()
# point4 = (1, 2) + (3, 4)
# point5 = tuple([1, 2])
# point6 = tuple("Hello World")
# point7 = (1, 2, 3)

# print(type(point))
# print(type(point2))
# print(type(point3))
# print(point4)
# print(point5)
# print(point6)
# print(point7[0:2])

# x, y, z = point
# if 10 in point:
#     print("exists")

# point[0] = 10


# Swapping Variables
# x = 10
# y = 11

# x, y = y, x  # under the hood we are defining a Tupple and unpacking it on the left side
# a, b = 1, 2

# print("x", x)
# print("y", y)


# Arrays
# Use arrays only if you are using large sequence of numbers #like 1000s
# items on the list otherwise use lists or tuples by default
# from array import array

# numbers = array("i", [1, 2, 3])
# numbers[0]


# Sets
# Sets is an unordered collection of unique items. We can't have duplicates and its

# numbers = [1, 1, 2, 3, 4]
# first = set(numbers)
# second = {1, 5}

# print(first | second)
# print(first & second)
# print(first - second)
# print(first ^ second)

# if 1 in first:
#     print("yes")


# Dictionaries - works like phone book phone -> contact or a
# A collection of key -> value pairs

# point = {"x": 1, "y": 2}
# point = dict(x=1, y=2)
# point = ["x"] = 10
# point = ["z"] = 20
# if "a" in point:
#     print(point["a"])
# print(point.get("a", 0))
# del point["x"]
# print(point)
# for key, value in point.items():
#     print(key, value)

# dictionary comprehensions
# values = []  # defining an empty list
# for x in range(5):  # iterating over this range object
#     values.append(
#         x * 2
#     )  # On each iteration you get the x multiplied by 2 and added to the list
# print(values)

# but with comprehensions this code will be like
# values = [x * 2 for x in range(5)] # this will give the same list output
# print(values)

# # We can also use the Comprehensions with Sets and dictionaries
# values = {x * 2 for x in range(5)}  # we get a Set of even numbers
# print(values)

# # Dictionary
# values = {x: x * 2 for x in range(5)}
# print(values)


# # Generator Expressions

# from sys import getsizeof

# values = (x * 2 for x in range(100))
# print("gen:", getsizeof(values))
# for x in values:
#     print(x)


# Unpacking Operator
# List
values = list(range(5))
values = [*range(5), *"Hello"]
print(values)


# Dictionaries

first = {"x": 1}
second = {"x": 10, "y": 2}
combined = {**first, **second, "z": 1}
print(combined)
