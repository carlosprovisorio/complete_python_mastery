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

list1 = [1, 2, 3]
list2 = [10, 20, 30]

print(list(zip(list1, list2)))
