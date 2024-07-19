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

high_income = False
good_credit = True
student = True

if high_income or good_credit or not student:
    print("Eligible")
