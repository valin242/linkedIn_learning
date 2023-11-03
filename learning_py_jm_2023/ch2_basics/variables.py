# Example of variables

# LinkedIn Learning Python course by Joe Marini

# Basic data types in Python: Numbers, Strings, Booleans, Sequences, Dictionaries
myint = 5
myfloat = 13.2
mystr = 'This is a string'
mybool = True
mylist = [0, 1, 'two', 3.2, False] # immutable: can't be changed
mytuple = (0, 1, 2) # immutable: can't be changed
mydict = {'one': 1, 'two': 2} # map unique keys to specific values

# print(myint)
# print(myfloat)
# print(mystr)
# print(mybool)
# print(mylist)
# print(mytuple)
# print(mydict)

# re-declaring a variable works
# myint = 'abc'
# print(myint)

# # to access a member of a sequence type, use []
# print(mylist[2])
# print(mytuple[1])

# # use slices to get parts of a sequence
# print(mylist[1:5])
# print(mylist[1:5:2]) # start:end:step


# # you can use the slices to reverse a sequence
print(mylist[::-1])

# dictionaires are accessed via keys
# print(mydict['one'])

# ERROR: varaibles of different types cannot be combined
# print("string type" + 123)
# print("string type" + str(123))

# Global vs. local varaibles in functions
# def someFunction():
#     global mystr
#     mystr = "def"
#     print(mystr)

# someFunction()
# print(mystr)

# del mystr # undefine variables in real time, removing the variable and its value
# print(mystr)
