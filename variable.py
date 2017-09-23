# Python Variable Types

'''
Variable are nothing by reserved memory locations to store values. When you create a variable you reserve some space in memory.
'''
age = 26 # integer
weight = 185 # floating point
name = "Thomas" # string

# print 'Name: '+ name 
# cannot concatenate 'str' and 'int' objects

# Multiple Assignment

a = b = c = "thomas"

# print a + b + c # should give thomasthomasthomas

# You can assign multiple variables using , and you can print multiple as well.

a,b,c = 1,2,"thomas"
# this is cleaner than below
d = 3; e = 4; f = "python"

# print a, b, c
# print d, e, f

#=============================================
# 5 Standard Data Types
# Numbers
# Strings
# List
# Tuple
# Dictionary

#=============================================
# Numbers
var1 = 1 # assign number to variable
del var1 # delete this variable. It is possible to delete multiple objects via listing variables with ,
# print var1 # should come back undefined

# 4 Types of Numbers 
# int (10, 100, -786)
# long (51924361L)
# float (0.0, 12.50, -21.3)
# complex (3e+26J)

# Display long integers with an uppercase L to avoid confusion with the number 1.
# Complex numbers consists of ordered pair of real floating point numbers denoted by x+yj. x and y are the real numbers and j is the imaginary unit. 

#=============================================
# Python Strings 
# identified via quotes. Subset of a string can be taken using the slice operator []. To get a subset range use [start index : end index]. 
# + is use for concatentation of strings
# * is used to repeat 

string = "Hello, World!"

# print (string[0:5] + " Thomas \n") * 2 # Should print out Hello, Thomas twice.

#=============================================
# Python Lists (arrays where items within the list can be different data types)
# list contains items seperated by commas and enclosed within [].
# these list can be accessed the same way a string can be. [] and [:]
# + is use for concatentation of strings
# * is used to repeat 

lists = [["hi again", 2], "hi", 1]

# print lists # [['hi again', 2], 'hi', 1]
# print lists[1:] # ['hi', 1]
# print lists[0][0] # hi again

#=============================================
# Python Tuples
# Similar to List but enclosed in (). They should be considered as a read only list meaning thier elemennts and size cannot be changed. 

tuple = (1, "hi" , "thomas")

# tuple[1] = "hello" # TypeError: 'tuple' object does not support item assignment

# print tuple[1:] #('hi', 'thomas')

# I'm curious...

tupleWithList = (["hi", "thomas"], 1, 2, ("goodbye", "thomas"))

tupleWithList[0][0] = "hello";

# print tupleWithList #(['hello', 'thomas'], 1, 2, ('goodbye', 'thomas')), pretty cool that this worked

#=============================================
# Python Dictionary
# kind of hash table type, they work like associative arrays/key-value pairs.
# Dictionaries are enclosed by curly braces {} and values are assigned and accessed via square braces [].
# To assign key value pairs to a dictionary use this key : value and , for multiple. 
# Dictionaries have no concept of order among element, they are not "out of order", they are simply unordered

dict = {
	1 : "hi, ",
	2 : 'thomas',
	3 : ''
}

dict[3] = "goodbye"
dict[4] = "thomas"

# print dict # {1: 'hi, ', 2: 'thomas', 3: 'goodbye', 4: 'thomas'}
# print dict.keys() # prints keys [1, 2, 3, 4]
# print dict.values() # prints values ['hi, ', 'thomas', 'goodbye', 'thomas']


#=============================================
# Data Type Conversion
# To convert between types simply use type name as a function 

# super curious!! tuple to list... 
cnvtTup = (1,2,3,["hello", "thomas"])

cnvtTup = list(cnvtTup)

cnvtTup[0] = 0
cnvtTup[1] = 1
cnvtTup[2] = 2

print cnvtTup






