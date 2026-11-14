from functools import reduce

# Lambda
add10 = lambda x: x + 10
a = add10(9)
print("Lambda:", a)

# Original list
numbers = [5, 7, 9, 10]

# Map
b = map(lambda x: x * 2, numbers)
print("Map:", list(b))

# Filter
c = filter(lambda x: x % 2 == 0, numbers)
print("Filter:", list(c))

# Reduce
d = reduce(lambda x, y: x * y, numbers)
print("Reduce:", d)