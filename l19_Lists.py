#!/usr/bin/python3

# Lists are a series of elemts separated by a comma inside of square brackets []

my_list = [1, 2, 3]

print( my_list )

# Can store objects of different types inside a list
my_list = ['string', 23, 1.2, 'o']

print( my_list )

# len() can also print the length of a list
print( len( my_list ) )

# Lists can also be indexed like strings.
my_list = ['one', 'two', 'three', 4, 5]
print( my_list[0] )

# You can slice lists just like strings as well
print( my_list[1:] )

print( my_list[:3] )

# You can also concatenate to lists just like strings
print( 'hello' + 'world' )

print( my_list + ['new_item'] )

# Permanently add to the list
my_list = my_list + ['permanent add']
print( my_list )

# You can also use '*' on lists
print( my_list * 2 )

l = [1, 2, 3]
print( l )

# Lists have methods associated with them
# Append to a list
l.append( 'append me!' )
print( l )

# Pop from a list (default is from end, but can specify from end)
# Pop returns the element removed
print( l.pop() )

x= l.pop(0)
print( x )
print( l )

print( l[1] )

# Indexing out of range will give an error!
# Uncomment below line to see error
# print( l[99] )

# Reversing and sorting lists
new_list = ['a', 'e', 'x', 'b', 'c']
print( new_list )
new_list.reverse()
print( new_list )
new_list.sort()
print( new_list )

# You can nest lists within lists!
l_1 = [1, 2, 3]
l_2 = [4, 5, 6]
l_3 = [7, 8, 9]
matrix = [l_1, l_2, l_3]
print( matrix )

# Indexing lists of lists requires an extra level of indexing
print( matrix[0] )
print( matrix[0][1] )
print( matrix[1][1] )
print( matrix[2][0] )

# List comprehension example ( Creating a list from a list )
first_col = [row[0] for row in matrix]
