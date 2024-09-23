## [PY-01] Introduction to Python ##

# Typing Python code #
2 + 2
a = 2 + 2
a
a = 7 - 2
a
b = 2 * 3
b - 1
b**2

# Python packages #
import math
math.sqrt(2)
from math import sqrt
sqrt(2)

# Numeric types #
type(a)
type(2.5)
type(2)
type(2.0)
2 + 2.5

# Boolean data #
d = 5 < a
d
type(d)
a == 4
math.sqrt(d)
1 - d

# Strings #
c = 'Messi'
type(c)
'Leo' + ' ' + 'Messi'

# Lists #
mylist = ['Messi', 'Cristiano', 'Neymar', 'Mbappé']
len(mylist)
newlist = mylist + [2, 3]
newlist
len(newlist)
mylist[0:2]
mylist[2:]
mylist[:3]

# Ranges #
myrange = range(0, 10, 2)
list(myrange)
list(range(5, 12))
list(range(10))

# Dictionaries #
my_dict = {'name': 'Joan', 'gender': 'F', 'age': 32}

# Functions #
def f(x):
    y = 1/(1 - x**2)
    return y
f(2)
f(1)
f('Mary')
def g(x, y):
    return x*y/(x**2 + y**2)
g(1, 1)
