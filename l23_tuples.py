#!/usr/bin/python3
"""This script is my following of the lesson on Tuples from the
   Udemy 'Complete Python Bootcamp' course. In it we will explore some of the
   basics of tuples."""

# Tuples are created similarly to lists, except using parentheses instead
# of square brackets
t = (1, 2, 3)
print(t)

# The same methods that can be called on lists can be called on lists
# can be called on tuples as well (there may be some exceptions)
print(len(t))
t = ('one', 2)
print(t)

# Tuples can be indexed just the same as lists as well, and slices are
# supported here too.
print(t[0])
print(t[1])
print(t[-1])
print(t[0:])

# There are of course methods associated with tuples as well.
# Here we see examples of index() and count()
print(t.index('one'))
print(t.index(2))
print(t.count('one'))

t = (1, 1, 2, 3)
print(t.count(1))
print(t.index(1))

# Tuples are immutable, which means that the elements within a tuple cannot
# changed after the tuple is initialized
l = [1, 2, 3]
print(l)
l[0] = 's'
print(l)
t = (1, 2, 3)
# Uncomment the line below to see an error showing the immutability
# of tuples
#t[0] = 's'
# Tuples can't grow either, so there is no method such as .append()
# like there is for lists
# Uncomment line below to see the error if we try to use an unsupported method
# t.append(4)
