import re

def parse_range(s, n, by=FALSE):
    y = 1
    if by:
        a, b, y = s.split(':')
        y = int(y)
    a = next(a, n)
    b = next(b, a)
    return list(range(a, b, y))

def next(s, last):
    l_s = len(s)
    l_last = len(str(last))
    if s[0] == '0':
        i =

def parse(s):
    split_ = s.split(',')
    numbers = [0]
    for item in split_:
        if item.count(':') == 2:
            parsed = parse_range(item, numbers[-1], by=TRUE)