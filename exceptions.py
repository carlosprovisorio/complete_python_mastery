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


# try:
#     age = int(input("Age: "))
#     xfactor = 10 / age
# except (ValueError, ZeroDivisionError):
#     print("You didn't enter a valid age.")
# else:
#     print("No exceptions were thrown.")


try:
    file = open("exceptions.py")
    age = int(input("Age: "))
    xfactor = 10 / age
except (ValueError, ZeroDivisionError):
    print("You didn't enter a valid age.")
else:
    print("No exceptions were thrown.")
finally:
    file.close()
