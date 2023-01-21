'''
'collections-use.py' contains useful imports from the 'collections' library with a few examples.

Library methods covered:
[
    deque,
    Counter,
    defaultdict
    OrderedDict
    namedtuple
]

Ref:
https://docs.python.org/3/library/collections.html
'''

##################################################################
##################################################################
from collections import deque
'''
'append()'
'appendleft()'
'clear()'
'copy()'
'count()'
'extend()'
'extendleft()'
'index()'
'insert()'
'maxlen()'
'pop()'
'popleft()'
'remove()'
'reverse()'
'rotate()'
'''

# Create a new deque
d = deque()

# Add elements to the deque
d.append(1)
d.appendleft(2)

# Remove elements from the deque
d.pop() # returns 1
d.popleft() # returns 2

# check the length of deque
len(d)

##################################################################
##################################################################
from collections import Counter
'''
'_keep_positive()'
'clear()'
'copy()'
'elements()'
'fromkeys()'
'get()'
'items()'
'keys()'
'most_common()'
'pop()'
'popitem()'
'setdefault()'
'subtract()'
'update()'
'values()'
'''

# Add to counter using the subscript notation:
c = Counter()
c['a'] += 1
c['b'] += 1
c['c'] += 3

# Add to Counter using the update() method:
c = Counter()
c.update(['a', 'b', 'c', 'c', 'c'])

# Add to Counter with the + or - operator to combine counters
c1 = Counter(['a', 'b', 'c'])
c2 = Counter(['b', 'c', 'c'])
c3 = c1 + c2
c4 = c1 - c2

# Create a new counter
c = Counter()                           # a new, empty counter
c = Counter('gallahad')                 # a new counter from an iterable
c = Counter({'red': 4, 'blue': 2})      # a new counter from a mapping
c = Counter(cats=4, dogs=8)             # a new counter from keyword args

# Counter common methods:
c.total()                       # total of all counts
c.clear()                       # reset all counts
list(c)                         # list unique elements
set(c)                          # convert to a set
dict(c)                         # convert to a regular dictionary
c.items()                       # convert to a list of (elem, cnt) pairs
Counter(dict(list_of_pairs))    # convert from a list of (elem, cnt) pairs
c.most_common()[:-n-1:-1]       # n least common elements
+c                              # remove zero and negative counts

# Set operations:
c = Counter(a=3, b=1)
d = Counter(a=1, b=2)
c + d                       # add two counters together:  c[x] + d[x]
c - d                       # subtract (keeping only positive counts)
c & d                       # intersection:  min(c[x], d[x])
c | d                       # union:  max(c[x], d[x])
c == d                      # equality:  c[x] == d[x]
c <= d                      # inclusion:  c[x] <= d[x]

##################################################################
##################################################################
from collections import defaultdict
'''
'clear()'
'copy()'
'default_factory()'
'fromkeys()'
'get()'
'items()'
'keys()'
'pop()'
'popitem()'
'setdefault()'
'update()'
'values()'
'''

# Using defaultdict to group a list of key-value pairs into a dictionary of lists:
'''
When each key is encountered for the first time, it is not already in the mapping; so an entry is automatically created using the default_factory function which returns an empty list. The list.append() operation then attaches the value to the new list. When keys are encountered again, the look-up proceeds normally (returning the list for that key) and the list.append() operation adds another value to the list. This technique is simpler and faster than an equivalent technique using dict.setdefault():
'''
# Method using collections 'defaultdict':
s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
d = defaultdict(list)
for k, v in s:
    d[k].append(v)

sorted(d.items()) # [('blue', [2, 4]), ('red', [1]), ('yellow', [1, 3])]

# Method with Python standard library:
d = {}
for k, v in s:
    d.setdefault(k, []).append(v)

sorted(d.items()) # [('blue', [2, 4]), ('red', [1]), ('yellow', [1, 3])]

# Example defaultdict with 'int' as the default_factory:
s = 'mississippi'
d = defaultdict(int)
for k in s:
    d[k] += 1

sorted(d.items()) # [('i', 4), ('m', 1), ('p', 2), ('s', 4)]

# Example defaultdict with 'set' as the default_factory:
s = [('red', 1), ('blue', 2), ('red', 3), ('blue', 4), ('red', 1), ('blue', 4)]
d = defaultdict(set)
for k, v in s:
    d[k].add(v)

sorted(d.items()) # [('blue', {2, 4}), ('red', {1, 3})]

##################################################################
##################################################################
from collections import OrderedDict
'''
'clear()'
'copy()'
'fromkeys()'
'get()'
'items()'
'keys()'
'move_to_end()'
'pop()'
'popitem()'
'setdefault()'
'update()'
'values()'
'''
# Create a new ordered dictionary
d = OrderedDict()

# Add elements to the ordered dictionary
d['first'] = 1
d['second'] = 2
d['third'] = 3

# Move an existing key to either end of an ordered dictionary. The item is moved to the right end if last is true (the default) or to the beginning if last is false.
d = OrderedDict.fromkeys('abcde')
d.move_to_end('b')
''.join(d) # 'acdeb'
d.move_to_end('b', last=False)
''.join(d) # 'bacde'

# Iterate over the items in the ordered dictionary
for key, value in d.items():
    print(key, value)

##################################################################
##################################################################
from collections import namedtuple
'''
'_asdict()'
'_field_defaults()'
'_fields()'
'_make()'
'_replace()'
'a()'
'b()'
'count()'
'index()'
'''

EmployeeRecord = namedtuple('EmployeeRecord', 'name, age, title, department, paygrade')

import csv
for emp in map(EmployeeRecord._make, csv.reader(open("employees.csv", "rb"))):
    print(emp.name, emp.title)

import sqlite3
conn = sqlite3.connect('/companydata')
cursor = conn.cursor()
cursor.execute('SELECT name, age, title, department, paygrade FROM employees')
for emp in map(EmployeeRecord._make, cursor.fetchall()):
    print(emp.name, emp.title)

# Use a list of strings as field names
Point = namedtuple("Point", ["x", "y"])
point = Point(2, 4)
point
Point(x=2, y=4)

# Access the coordinates
point.x # 2
point.y # 4
point[0] # 2

# Use a generator expression as field names
Point = namedtuple("Point", (field for field in "xy"))
Point(2, 4)
Point(x=2, y=4)

# Use a string with comma-separated field names
Point = namedtuple("Point", "x, y")
Point(2, 4)
Point(x=2, y=4)

# Use a string with space-separated field names
Point = namedtuple("Point", "x y")
Point(2, 4)
Point(x=2, y=4)

# Define default values for fields
Person = namedtuple("Person", "name job", defaults=["Python Developer"])
person = Person("Jane")

# Create a dictionary from a named tuple
person._asdict()

# Replace the value of a field
person = person._replace(job="Web Developer")