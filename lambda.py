# Lambda Functions in Python

# Addition
add = lambda a, b: a + b
print("Addition:", add(5, 3))

# Square
square = lambda x: x * x
print("Square:", square(6))

# Even check
is_even = lambda x: x % 2 == 0
print("Is 10 even?", is_even(10))

# Using map
numbers = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x * x, numbers))
print("Squares:", squares)

# Using filter
evens = list(filter(lambda x: x % 2 == 0, numbers))
print("Even Numbers:", evens)