# A simple generator function
def my_gen():
    n = 1
    print('This is printed first')
    # Generator function contains yield statements
    yield n

    n += 1
    print('This is printed second')
    yield n

    n += 1
    print('This is printed at last')
    yield n


# Using for loop
for item in my_gen():
    print(item)

"""
output:
    This is printed first
    1
    This is printed second
    2
    This is printed at last
    3
"""

def rev_str(my_str):
    length = len(my_str)
    for i in range(length - 1, -1, -1):
        yield my_str[i]


# For loop to reverse the string
for char in rev_str("hello"):
    print(char)

"""
output:
    o
    l
    l
    e
    h
"""

#___________________________________________________________________________________
#this powtwo method is not a generator but is equivalent to the generator function PowTwoGen
class PowTwo:
    def __init__(self, max=0):
        self.n = 0
        self.max = max

    def __iter__(self):
        return self

    def __next__(self):
        if self.n > self.max:
            raise StopIteration

        result = 2 ** self.n
        self.n += 1
        return result

def PowTwoGen(max=0):
    n = 0
    while n < max:
        yield 2 ** n
        n += 1