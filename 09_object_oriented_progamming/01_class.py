class Employee:
    language = "Py"  # This is a class attribute
    salary = 120000


harry = Employee()
harry.name = "Harry"  # This is an instance attribute
print(harry.name, harry.language, harry.salary)

rohan = Employee()
rohan.name = "Rohan Roro Robinson"
print(rohan.name, rohan.salary, rohan.language)


# Here name is instance attribute and salary and language
# attributes as they directly belong to the class
