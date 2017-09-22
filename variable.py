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

# NUMBERS
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
#Python Strings 
# identified via quotes. Subset of a string can be taken using the slice operator []. To get a subset range use [start index : end index]. 
# + is use for concatentation of strings
# * is used to repeat 

string = "Hello, World!"

print (string[0:5] + " Thomas \n") * 2 # Should print out Hello, Thomas twice.






