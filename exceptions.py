# Exception
# numbers = [1, 2]
# print(numbers[3])  # it generates an error by the developer

try:
    age = int(input("Age: "))
except ValueError:
    print("You didn't enter a valid age.")
else:
    print("No exceptions were thrown.")
print("Execution continues.")
