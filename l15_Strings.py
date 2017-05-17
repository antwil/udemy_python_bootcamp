#!/usr/bin/python3

# Single word
print( 'hello' )

# Entire phrase
print( 'This is also a string' )

# We can also use double quotes
print( "String built with double quotes" )

# Be careful with quotes!
# Unquote the below line to see the error that occurs
#print( ' I'm using singe quotes, but will create an error' )

# Proper way to use single quotes inside a string
print( "Now I'm ready to use single quotes inside a string!" )

# We can simply declare a string
'Hello World'

# Printing new lines
print( 'Hello World 1' )
print( 'Hello World 2' )
print( 'Use \n to print a new  line' )
print( '\n' )
print( 'See what I mean?' )

# In python2 'print' is a statement
# can just call "print 'String'" in python2
# To use print function from python2 in python 3
#from __future__ import print_function
print( 'Hello World' )

# Checking the length of a string
print( len( 'Hello World' ) )

# String indexing

# Assign s as a string
s = 'Hello World'

print( s )

# Show first element (in this case a letter)
print( s[0] )

print( s[1] )

print( s[2] )

# Can perform string slicing using ':'
# This grabs everything up to a certain point

# Grab everything pase the first term all the way to the length of s
print( s[1:] )

# 's' remains unchanged with the slicing operation
print( s )

# Grab everything up to (and not including) index 3
print( s[:3] )

# Everything
print( s[:] )

# Last letter (one index behind 0 so it loops back around)
print( s[-1] )

# Grab everything but the last letter
print( s[:-1] )

# Can also specify step size using 2 colons

# Grab everything, going in step size of 1
print( s[::1] )

# Grab everything, going in step size of 2
print( s[::2] )

# We can use this to print a string backwards
print( s[::-1] )

# Strings are immutable, which means once a string object has been created,
# the elements within it cannot be changed or replaced

print( s )

# Trying to change the first letter to 'x' will cause an error
# Uncomment below line to see error
#s[0] = 'x'

# We can concatenate strings (adds a string to the end of another string)
# This creates a new string object

print( s )

# Concatenate two strings
print( s + ' concatenate me!' )

# We can reassign s completely as well with concatenation
s = s + ' concatenate me!'
print( s )

# We can use multiplication symbol to create repetition
letter = 'z'
print( letter*10 )

# String objects have built in utility methods
print( s )

# Upper case a string
print( s.upper() )

# Lower case a string
print( s.lower() )

# Split a string (split on blank space is default)
print( s.split() )

# Split on a specific character
print( s.split( 'W' ) )

# Can use .format() method to add formatted objects to string statements
print( 'Insert another string with curly brackets: {}'.format( 'The inserted string' ) )
