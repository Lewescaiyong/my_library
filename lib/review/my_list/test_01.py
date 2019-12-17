#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random


a = range(1, 6)
print a[::2]
print a[-2:]
print sum([i + 3 if a.index(i) % 2 == 0 else i for i in a])
random.shuffle(a)
b = a[:]
b.sort()
print a
print b
print zip(a, b)
print dict(zip(a, b))