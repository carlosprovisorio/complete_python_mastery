# Exception
# numbers = [1, 2]
# print(numbers[3])  # it generates an error by the developer

# try:
#     age = int(input("Age: "))
# except ValueError:
#     print("You didn't enter a valid age.")
# else:
#     print("No exceptions were thrown.")
# print("Execution continues.")

# Handling Exceptions

# try:
#     age = int(input("Age: "))
#     xfactor = 10 / age
# except (ValueError, ZeroDivisionError):
#     print("You didn't enter a valid age.")
# else:
#     print("No exceptions were thrown.")

# cleaning Up

# try:
#     file = open("exceptions.py")
#     age = int(input("Age: "))
#     xfactor = 10 / age
# except (ValueError, ZeroDivisionError):
#     print("You didn't enter a valid age.")
# else:
#     print("No exceptions were thrown.")
# finally:
#     file.close()


# The with Statement
# try:
#     with open("exceptions.py") as file:
#         print("File opened.")

#     age = int(input("Age: "))
#     xfactor = 10 / age
# except (ValueError, ZeroDivisionError):
#     print("You didn't enter a valid age.")
# else:
#     print("No exceptions were thrown.")


# Cost of raising exceptions

from timeit import timeit

code1 = """def calculate_xfactor(age):
    if age <= 0:
        raise ValueError("Age cannot be 0 or less.")
    return 10 / age


try:
    calculate_xfactor(-1)
except ValueError as error:
    pass
"""

code2 = """def calculate_xfactor(age):
    if age <= 0:
        return None
    return 10 / age


xfactor = calculate_xfactor(-1)
if xfactor == None:
    pass
"""

print("first_code=", timeit(code1, number=10000))
print("first_code=", timeit(code2, number=10000))
