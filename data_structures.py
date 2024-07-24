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

numbers = [1, 2, 3, 4, 4, 4, 4, 4, 9]
# first, second, *other = numbers
first, *other, last = numbers
print(first, last)
print(other)