#!/usr/bin/python3

print( 'This is a string' )

s = 'STRING'
print( 'Place another string with a mod and s: %s' %(s) )


# Format floating point numbers with '%#1.#2f'
#  #1 = minimum number of digits string should contain
#  #2 = number of digits to display after the decimal point
print( 'Floating point numbers: %1.2f' %(13.144) )

print( 'Floating point numbers: %1.0f' %(13.144) )

print( 'Floating point numbers: %1.5f' %(13.144) )

print( 'Floating point numbers: %10.2f' %(13.144) )

print( 'Floating point numbers: %25.2f' %(13.144) )

# There are two different conversion format methods, %s and %r
#  %s uses str() method to convert object to string
#  %r uses repr() method to convert object to string
print( 'Here is a number: %s. Here is a string: %s' %(123.1, 'hi') )

print( 'Here is a number: %r. Here is a string: %r' %(123.1, 'hi') )

# The %() is a tuple and should contain as many elements as
# there are format operators (%f, %s, %d, etc.)
# An example with 3...
print( 'First: %s, Second: %1.2f, Third: %r' %('hi!', 3.14, 22) )

# You can also format string using the string.format() method
print( 'This is a string with an {p}'.format(p='insert') )

# You can insert more than once in the same format string
print( 'One: {p}, Two: {p}, Three: {p}'.format( p='Hi!' ) )

# Even several different objects
print( 'Object 1: {a}, Object 2: {b}, Object 3: {c}'.format( a=1, b='two', c=12.3 ) )
