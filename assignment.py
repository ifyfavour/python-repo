"""
#1. How do you declare a variable in Python? Provide an example.
A variable is created when some value is assigned to it. 
The value assigned to a variable determines the data type of that variable.
variable consist of the name, assignment operator (=) and the data 
#2. What are the rules for naming variables in Python?
* python does not accept a varible starting with numbers
* python does not accept special characters in creating a variable
* in naming a variable python is cae sensitve
#3. What are the basic data types in Python? Give examples of each.
*Numeric data types-
- int (whole numbers till infinity(4,5,6,33,6))
- float (decimal numbers (22.4,5.6,44,5))
- complex (combination of int and float(444.0j))
#4. How do you convert one data type to another in Python? Provide an example.
type of conversion or casting are as follows
- Implicit conversion
- Explicit conversion
#5. What is type conversion in Python? Why is it necessary?
* Type conversion is used to convert datatype to the other
#6. Describe the difference between implicit and explicit type conversion in Python.
- Implicit conversion: is authomatic
- Explicit conversion: is clearly stated and direct
#7. What is the purpose of using comments in Python? Give an example.
* comments are used to make information private (it cannot not be testrun)
* It can serve as a reminder e.g 
# to name variable
name = input("What is your name?")
print(name)
#8. Explain the concept of dynamic typing in Python and its implications for variable declaration and usage.
* Dynamic typing in Python means variables can hold values of any type, determined at runtime. Declarations are implicit, allowing flexibility but requiring careful handling to prevent unexpected behavior.
#9. How do you check the data type of a variable in Python?
* You can check the data type using *type()* function example 
variable = 34
print(type(variable))
#10. What are some common built-in functions used for type conversion in Python, and how do you use them?
* bool(): Converts a value to a boolean.
* str(): Converts a value to a string.
* int(): Cnverts a value to integer.
* list(): Converts a value to list
#11. Discuss the significance of using meaningful variable names in Python programming. Provide an example.
* Readability: Meaningful variable names make your code easier to understand for both yourself and others who may read your code. Descriptive names provide context and clarity, reducing the need for comments to explain the purpose of variables.
* Maintainability: When you revisit your code later or need to make modifications, meaningful variable names help you quickly grasp the purpose of each variable and its role within the code. This makes maintenance and debugging more efficient.
* Documentation: Well-chosen variable names act as self-documentation for your code. They serve as a form of inline documentation, providing insights into the functionality of your program without the need for additional comments.
* Reduced Errors: Meaningful variable names can help prevent errors caused by misunderstandings or confusion about the purpose of variables. When variables have clear names that reflect their intended use, it's less likely that you'll misuse or misunderstand them.
"""