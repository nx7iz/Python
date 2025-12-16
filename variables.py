students_count = 1000
rating = 4.99
is_published = False
course_name = """
Multiple
Lines
"""

# x = 1
# y = 2
# x, y = 1, 2

# x = y = 1
# x = [1, 2, 3]
# print(id(x))

# x.append(4)
# print(id(x))

# course = "Python Programming"
# print(len(course))
# print(course[0])
# print(course[-1])
# print(course[0:3]) #slice(remove) from start:end
# print(course[:3]) # default   value of 0
# print(course[0:]) # default value of len of string
# print(course[:])


# # \" \' \\ \n
# message = "Python \"Programming\""
# print(message)

# first = "Helios"
# last = "Zelar"
# full = f"{first} {last}"
# print(full)

# Strings
# course = "    Python Programming     "
# print(course.upper())
# print(course.lower())
# print(course.title())

# print(course.strip())

# print(course.find("pro")) # returns index

# print("Programming" in course)
# print("Programming" not in course)

# Numbers
# x = 10
# # x = 0b1010
# print(bin(x)) # to give the binary representation of a number

# x =  0x12c
# print(hex(x))

# # a + bi
# x = 1 + 2j
# print(x)


# x = 10 + 3
# x = 10 - 3
# x = 10 * 3
# x = 10 / 3 # division of floating
# x = 10 // 3 # division for ints
# x = 10 % 3 # modulo returns the remainder
# x = 10 ** 3 # left to the power right (10 to the power 3)

# x = x + 1
# x += 1 # Augmented assignment operator

# print(x)

# Working with numbers

# import math

# PI = 3.14
# print(round(PI))
# print(abs(PI))

# print(math.floor(PI))

# Type Conversion
# x = input("x: ")
# # y = x + 1

# # Type conversion
# print(int(x))
# print(float(x))
# print(bool(x))
# # str(x)
# # Falsy -> "", 0, [], None(null)

# Conditional Statements
# age = 22
# if age >= 18:
#     print("Adult")
#     print("Adult")
# elif age >= 13:
#     print("Teenager")
# else:
#     print("Child")

# print("All done!")

# Logical Operators
# and or not
# name = " "
# if not name.strip():
#     print("Name is empty")

# age = 22
# # if 18 <= age < 65: # chaining comparision operators
# #     print("You are eligible")

# if age >= 18:
#     message = "Eligible"
# else:
#     message = "Not eligible"

# Ternary operator
# message = "Eligible" if age >= 18 else "Not eligible"
# print(message)

# For Loops

# for x in "Python":
#     print(x)

# for x in ['a', 'b', 'c']:
#     print(x)

# for x in range(0, 10, 2):
#     print(x)

# print(type(range(5)))


# For-Else
# names = ['John', 'Bob', 'Mosh', 'Sarah']
# for name in names:
#     if name.startswith("J"):
#         print("Found!")
#         break
# else:
#     print("Not found!")

# While
# guess = 0
# answer = 5

# while answer != guess:
#     guess = int(input("Guess: "))
# else:
#     pass

# Functions
# def increment(number: int, by: int=1) -> tuple:
#     return number, number + by


# print(increment(2))

# *args. wait, what?
# def multiply(*list):
#     total = 1
#     for number in list:
#         total *= number
#     return total


# print(multiply(2, 3, 4, 5))

# **args


# def save_user(**user):
#     print(user["name"])


# save_user(id=1, name='Admin')

# def greet():
#     message = "a"

# def multiply(*numbers):
#     total = 1
#     for number in numbers:
#         total *= number
#     return total


# print("Start")
# print(multiply(2, 3, 4))
# print("Finish")


def fizz_buzz(input):
    pass
    if (input % 3 == 0) and (input % 5 == 0):
        return "FizzBuzz"
    if input % 3 == 0:
        return "Fizz"
    if input % 5 == 0:
        return "Buzz"
    return input


print(fizz_buzz(3))
