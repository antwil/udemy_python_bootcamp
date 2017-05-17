#!/usr/bin/python3

# Addition
print( 2+1 )

# Subtraction
print( 2-1 )

# Multiplication
print( 2*2 )

# Division
print( 3/2 ) # In python2 this would equal 1

# How to get around "classic" diviision in python2
print( 3.0/2 )

# or
print( 3/2.0 )

# or
print( float(3)/2 )

# or
# from __future__ import division
print( 3/2 )

# Powers
print( 2**3 )

# Square roots too! (using powers)
print( 4**0.5 )

# Order of operations followed in Python
print( 2 + 10 * 10 + 3 )

# Can also use parenthesis to specify orders
print( (2+10) * (10+3) )

# Variable assignment
a = 5

print( a+a )

# Reassignment
a = 10

print( a )

# Reassign using variale itself
a = a + a

print( a )

# More complex variable names and assignments
my_income = 100

tax_rate = 0.1

my_taxes = my_income * tax_rate

print( my_taxes )

# Floating points aren't always 100% accurate...
print( 0.1 + 0.2 - 0.3 )