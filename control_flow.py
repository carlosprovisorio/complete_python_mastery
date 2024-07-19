# Comparison Operators

# print(10 > 3)
# print(10 >= 3)
# print(10 < 20)
# print(10 <= 20)
# print(10 == 10)
# print(10 == "10")
# print(10 != 10)


# Conditional Statement
# temperature = 15

# if temperature > 30:
#     print("It's warm")
#     print("Drink water")
# elif temperature > 20:
#     print("It's nice")
# else:
#     print("It's cold")
# print("Done")

# age = 22
# if age >= 18:
#     print("Eligible")
# else:
#     print("Not Eligible")

# age = 40
# if age >= 30:
#     message = "Eligible"
# else:
#     message = "Not Eligible"
# print(message)

# # Ternary Operator
# age = 15
# message = "Eligible" if age >= 18 else "Not Eligible"
# print(message)

# Logical Operators

# high_income = True
# good_credit = True

# if high_income and good_credit:
#     print("Eligible")

# high_income = False
# good_credit = True

# if high_income or good_credit:
#     print("Eligible")
# else:
#     print("Not Eligible")


# high_income = False
# good_credit = True
# student = True

# if not student:
#     print("Eligible")
# else:
#     print("Not Eligible")


# high_income = False
# good_credit = True
# student = False

# if (high_income or good_credit) and not student:
#     print("Eligible")
# else:
#     print("Not Eligible")

# Short-circuit Evaluation

# high_income = False
# good_credit = True
# student = True

# if high_income or good_credit or not student:
#     print("Eligible")


# Chaining comparison

# age should be between 18 and 65

# age = 22
# if 18 <= age < 65:
#     print("Eligible")


# # Quiz
# if 10 == "10":
#     print("a")
# elif "bag" > "apple" and "bag" > "cat":
#     print("b")
# else:
#     print("c")

# For loops

# for number in range(3):
#     print("Attempt")

# for number in range(1, 4):
#     print("Attempt", number, number * ".")


# for number in range(1, 20, 2):
#     print("Attempt", number, number * ".")


# For..Else
# successful = True
# for number in range(3):
#     print("Attempt")
#     if successful:
#         print("Successful")
#         break


# successful = False
# for number in range(3):
#     print("Attempt")
#     if successful:
#         print("Successful")
#         break
#     else:
#         print("Attempted 3 times and failed")


# Nested Loops
# for x in range(5):
#     for y in range(3):
#         print(f"({x}, {y})")

# for carlos in range(5):
#     for carol in range(3):
#         print(f"({carlos}, {carol})")

# Iterables
# for x in "Python":
#     print(x)

# for y in [1, 2, 3, 4, 5]:
#     print(y)

# While Loops
# number = 100
# while number > 0:
#     print(number)
#     number //= 2

# command = ""
# while command.lower() != "quit":
#     command = input(">")
#     print("ECHO", command)

# while True:
#     command = input(">")
#     print("ECHO", command)
#     if command.lower() == "quit":
#         break


# Quizz - my solution
# for number in range(2, 10, 2):
#     print(number)
# print("We have 4 even numbers")

# expected answer
count = 0
for number in range(1, 10):
    if number % 2 == 0:
        count += 1
        print(number)
print(f"We have {count} even numbers")
