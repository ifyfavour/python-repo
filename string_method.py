'''STRING METHODS'''

"""Method	Description"""
#capitalize()	Converts the first character to upper case
name = input("Dear customer your firstname is required ").capitalize()
print(f'{name}')
#casefold()	Converts string into lower case
what = input("What's your name").casefold()
print(f'{what}')
#center()	Returns a centered string
fruit = 'pawpaw,' 'banana'
a = fruit.center(12)
print(a)
#count()	Returns the number of times a specified value occurs in a string
Sentence = ["'apple' 'banana' 'apple'"].count('apple')
print(f'{Sentence}')
#encode()	Returns an encoded version of the string
favour = 'my name is favour'
a = favour.encode()
print(a)
#endswith()	Returns true if the string ends with the specified value
baby = "my baby is anabella."
d = baby.endswith(
    '.'
)
print(d)
#expandtabs()	Sets the tab size of the string
tabs ='H\te\tl\tl\to\t!'
a = tabs
print(a.expandtabs())

# find() Searches the string for a specified value and returns the position of where it was found
text = "my God is good to me"
dt = text.find("God")
print(dt)
#format()	Formats specified values in a string
txt = "For only"
price = 49
print(f" {txt} {price:.5f} naira" )
#format_map()	Formats specified values in a string
#index()	Searches the string for a specified value and returns the position of where it was found
hell = "Hello, welcome to my world."
x = hell.index("welcome")
print(x)

'''isalnum()	Returns True if all characters in the string are alphanumeric
isalpha()	Returns True if all characters in the string are in the alphabet
isascii()	Returns True if all characters in the string are ascii characters
isdecimal()	Returns True if all characters in the string are decimals
isdigit()	Returns True if all characters in the string are digits
isidentifier()	Returns True if the string is an identifier
islower()	Returns True if all characters in the string are lower case
isnumeric()	Returns True if all characters in the string are numeric
isprintable()	Returns True if all characters in the string are printable
isspace()	Returns True if all characters in the string are whitespaces
istitle()	Returns True if the string follows the rules of a title
isupper()	Returns True if all characters in the string are upper case
join()	Joins the elements of an iterable to the end of the string
ljust()	Returns a left justified version of the string
lower()	Converts a string into lower case
lstrip()	Returns a left trim version of the string
maketrans()	Returns a translation table to be used in translations
partition()	Returns a tuple where the string is parted into three parts
replace()	Returns a string where a specified value is replaced with a specified value
rfind()	Searches the string for a specified value and returns the last position of where it was found
rindex()	Searches the string for a specified value and returns the last position of where it was found
rjust()	Returns a right justified version of the string
rpartition()	Returns a tuple where the string is parted into three parts
rsplit()	Splits the string at the specified separator, and returns a list
rstrip()	Returns a right trim version of the string
split()	Splits the string at the specified separator, and returns a list
splitlines()	Splits the string at line breaks and returns a list
startswith()	Returns true if the string starts with the specified value
strip()	Returns a trimmed version of the string
swapcase()	Swaps cases, lower case becomes upper case and vice versa
title()	Converts the first character of each word to upper case
translate()	Returns a translated string
upper()	Converts a string into upper case
zfill()	Fills the string with a specified number of 0 values at the beginning'''