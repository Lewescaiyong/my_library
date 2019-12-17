#!/usr/bin/env python
# -*- coding: utf-8 -*-


a = {'a': 'a', 'b': 'b'}
b = {'c': 'c', 'd': 'd'}

print a.items()
print a.keys()
print a.values()
a.update(b)
print a
print a.pop('e', None)
print a
