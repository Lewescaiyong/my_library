#!/usr/bin/env python
# -*- coding: utf-8 -*-


a = list('abcdef')
b = range(10)

print a + b
print a * 2
print a[0]
print a[1:]
a.reverse()
print a
a.sort()
print a
a.remove('c')
print a
del a[0]
print a
del a[:1]
print a
a.pop(0)
print a
a.append(1)
print a
a.extend(b)
print a
c = list(set(a))
c.sort()
print c