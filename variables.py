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

course = "    Python Programming     "
print(course.upper())
print(course.lower())
print(course.title())

print(course.strip())

print(course.find("pro")) # returns index

print("Programming" in course)
print("Programming" not in course)