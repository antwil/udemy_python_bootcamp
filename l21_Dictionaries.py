#!/usr/bin/python3

# Dictionaries are initialized with curly brackets,
# and entries are of the form key:value
my_dict = {'key1':'value1', 'key2':'value2'}

# To get an entry index the dictionary just like
# you would a string or list. Use a key to index
# the dictionary to get its corresponding value.
print( my_dict['key2'] )

# Values can me of multiple different types
my_dict = {'key1':123, 'key2':[12, 23, 33], 'key3':['item1', 'item2', 'item3']}
print( my_dict['key3'] )

# If a dictionary value is a list, you can call an index on it
print( my_dict['key3'][0] )

# And then even a method on that value. Really you can continue
# chaining operations until a value is a basic type such as an
# integer or a character.
print( my_dict['key3'][0].upper() )

# You can also edit the values of a dict after it is created
print( my_dict['key1'] )
my_dict['key1'] = my_dict['key1'] - 123
print( my_dict['key1'] )

# Pyton, like most languages if you know others, can do self
# self-assignment operators (e.g. +=, *=, etc.)
my_dict['key1'] -= 123
print( my_dict['key1'] )

# You can also assign keys outside of the initialization of the dictionary
d = {}
d['animal'] = 'Dog'
d['answer'] = 42
print( d )

# You can also nest a dictionary inside of another dictionary
d = {'key1':{'nestkey':{'subnestkey':'value'}}}
print( d )
# Can index keys as long as there are nested dictionaries
print( d['key1']['nestkey']['subnestkey'] )

# And of course, dictionaries have methods associated with them as well
d = {'key1':1,'key2':2,'key3':3}
print( d )

# Return a list of all keys in a dictionary
print( d.keys() )

# Now grab all the values
print( d.values() )

# Return key value pairs (tuples)
print( d.items() )