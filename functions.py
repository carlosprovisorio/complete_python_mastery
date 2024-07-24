# Defining functions
# Arguments
# def greet(first_name, last_name):
#     print(f"Hi {first_name} {last_name}")
#     print("Welcome aboard")


# greet("Carlos", "Ferreira")


# Type of functions
# 1 - Perform a task
# 2 - Return a value


# def get_greeting(name):
#     return f"Hi {name}"


# message = get_greeting("Carlos")
# print(message)


# def increment(number, by):
#     return number + by


# print(increment(2, by=1))


# Default Arguments
# def increment(number, by=1):
#     return number + by


# print(increment(2, 5))


# Xargs
# def multiply(*numbers):
#     total = 1
#     for number in numbers:
#         total *= number
#     return total


# print(multiply(2, 3, 4, 5))

# xxargs


# def save_user(**user):
#     print(user)


# save_user(id=1, name="John", age=22)


# def save_user(**user):
#     print(user["id"])


# save_user(id=1, name="john", age=22)


# Scope
# message = "a"  # global variable


# def greet(name):
#     global message #bad practice
#     message = "b"


# greet("Carlos")
# print(message)


# def multiply(*numbers):
#     total = 1
#     for number in numbers:
#         total *= number
#     return total


# print("Start")
# print(multiply(1, 2, 3))

# click on the line to add a breakpoint
# F5 to initiate the debugger
# F10 to move to the next line
# F11 to jump to the beginning of the function
# Shift F11 to skip the debugger before it execute all lines


def fizz_buzz(input):
    if (input % 3 == 0) and (input % 5 == 0):
        return "FizzBuzz"
    if input % 3 == 0:
        return "Fizz"
    if input % 5 == 0:
        return "Buzz"
    return input


print(fizz_buzz(15))
