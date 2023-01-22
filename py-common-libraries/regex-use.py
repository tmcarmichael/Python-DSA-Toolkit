'''
'regex-use.py' contains a useful subset of imports from the 'regex' lib with a few examples.

Library methods covered:
[
  compile,
  search,
  match,
  fullmatch,
  split,
  findall,
  sub,
  escape
]

Ref:
https://docs.python.org/3/library/re.html
'''

import re
##################################################################
##################################################################
# compile - compile a pattern into a regular expression object

r = re.compile('[a-z]')
r.match('a') # <re.Match object; span=(0, 1), match='a'>

##################################################################
##################################################################
# search - if pattern is found anywhere in the string

m = re.search('[a-z]', 'abc') # <re.Match object; span=(0, 1), match='a'>
m.group(0) # 'a'

##################################################################
##################################################################
# match - if part of string matches the pattern

m = re.match('[a-z]', 'abc') # <re.Match object; span=(0, 1), match='a'>
m.group(0) # 'a'

##################################################################
##################################################################
# fullmatch - if whole string matches the pattern

m = re.fullmatch('[a-z]', 'abcJ') # None
m.group(0) # Error (NoneType has no attribute 'group'

m = re.fullmatch('[a-z]', 'abc') # <re.Match object; span=(0, 3), match='abc'>
m.group(0) # 'abc'

##################################################################
##################################################################
# split - split string by the occurrences of pattern

s = re.split('[a-z]', 'aD&*^b') # ['', 'D&*^', '']

##################################################################
##################################################################
# findall - find all occurrences of pattern in string

s = re.findall('[a-z]', 'abc def GHI JKL') # ['a', 'b', 'c', 'd', 'e', 'f']

##################################################################
##################################################################
# sub - replace all occurrences of pattern in string with repl

s = re.sub('[a-z]', 'Z', 'abc def GHI JKL') # 'ZZZ ZZZ GHI JKL'

##################################################################
##################################################################
# escape - escape all the characters in pattern

s = re.escape('abc def GHI JKL') # 'abc\\ def\\ GHI\\ JKL'