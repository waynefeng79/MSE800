# Registering decorated objects to an APIfrom __future__ import print_function # 2.X

# Initializes an empty dictionary named registry, acting as our central database to store the decorated functions and classes
registry = {}

# define a decorator to register function and class
def register(obj):  # Both class and func decorator
    registry[obj.__name__] = obj    # Add to registry
    return obj      # Return obj itself, not a wrapper

@register           # spam = register(spam)
def spam(x):        # define a function decorated by register
    return(x ** 2)  # return function result

@register           # ham = register(ham)
def ham(x):         # define a function decorated by register
    return(x ** 3)  # return function result

@register           # Eggs = register(Eggs)
class Eggs:         # Eggs return as is
    def __init__(self, x):    # constructor
        self.data = x ** 4    # field variable assignment

    def __str__(self):        # Stringfy object
        return str(self.data) # print self.data on object print

print('Registry:')
# For each registered function and class, print the dictionary values
for name in registry:
    print(name, '=>', registry[name], type(registry[name]))

print('\nManual calls:')
print(spam(2))      # Original function called directly (not intercepted)
print(ham(2))       # Original function called directly (not intercepted)
X = Eggs(2)         # Create an Egg instance with original Eggs class
print(X)            # Print the stringfied object

print('\nRegistry calls:')
for name in registry:
    print(name, '=>', registry[name](2))    # Invoke function from registry, and print created object from class
