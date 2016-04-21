"""All Python code for Five Weird Python Tricks presentation."""


# 1
# Tuple Unpacking

tup = ('a', 'b', 'c')
a, b, c = tup

print(a)
print(b)
print(c)

# Should be called sequence unpacking

a, b, c = ['a', 'b', 'c']
print(a)
print(b)
print(c)

a, b, c = 'abc'
print(a)
print(b)
print(c)


# Useful in many situations
# Example: you expect a certain number of items from str.split()

try:
    request = 'GET /login.html HTTP/1.1'
    method, uri, protocol = request.split()

except ValueError:
    print('400 Bad Request!')


# 2
# Iterate over a dictionary

dictionary = {'a': 0, 'b': 1, 'c': 2, 'd': 3}


# Not So Good:

for key in dictionary:
    value = dictionary[key]
    print('{}: {}'.format(key, value))

# Much Better:

for key, value in dictionary.items():
    print('{}: {}'.format(key, value))

print(dictionary.items())


# 3
# Iterating over an ordered sequence (list, tuple, string, etc.)

a_list = [5, 2, ('x', 'y'), 7.7, 9, 'c', 10, 2, 'a']

# Really Bad:

for index in range(len(a_list)):
    print(a_list[index])

# Better:

for item in a_list:
    print(item)


# But what if you need the index AND the item?


# Still Really Bad:

for index in range(len(a_list)):
    print('Item at index {} is {}'.format(index, a_list[index]))

# Best Ever:

for index, item in enumerate(a_list):
    print('Item at index {} is {}'.format(index, item))


# 4
# Multi-Assignment

a = 'a'
b = 'b'

# How could you swap these values? Use an intermediate?

c = a
a = b
b = c
print('a = {}'.format(a))
print('b = {}'.format(b))

# But why use 3 lines when you can use only one?

a, b = b, a
print('a = {}'.format(a))
print('b = {}'.format(b))


# Useful for swapping items in a list:

a_list = [1, 2, 3, 4]
a_list[0], a_list[1] = a_list[1], a_list[0]
print(a_list)


# Or even reversing a Linked List in one line!

def reverse_linked_list(linked_list):
    """Reverse a Linked List and return it."""
    node1 = linked_list.head
    node2 = linked_list.head.next
    while node2.next:
        node2.next, node2, node1 = node1, node2.next, node2

    return node2


# 5.
# Bools are Ints are Bools


# OK:

print('a string' * 2)

# Not OK:

try:
    print('a string' + 2)
except TypeError:
    print('Not OK!')

# What about bools?

print(1 + False)
print(1 + True)

# *record scratch* Whaaaaat?

print(10 * True)
print(10 * False)


# Bools are ints are bools are ints!

# How is this useful?
# Counting things based on a boolean property

list_of_nums = [7, 2, 0, 3, 99, 11]
insert_num = 10

insertion_index = sum(num < insert_num for num in list_of_nums)

print(insertion_index)


# Adding a string or not

for n in range(16):
    divides_by_3 = n % 3 == 0  # Boolean statement
    divides_by_5 = n % 5 == 0  # Boolean statement

    fizz = 'Fizz' * divides_by_3  # str * bool
    buzz = 'Buzz' * divides_by_5  # str * bool

    fizzbuzz = fizz + buzz
    print(fizzbuzz or n)


# One line for your mind:

for n in range(16):
    print('Fizz' * (n % 3 == 0) + 'Buzz' * (n % 5 == 0) or n)
