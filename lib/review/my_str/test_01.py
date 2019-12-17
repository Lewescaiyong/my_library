#!/usr/bin/env python
# -*- coding: utf-8 -*-


result = list()

with open(r'F:\python\project\learnmysql\Practice\review\my_str\str_options.py') as f:
    a = f.read().split()
    print(a)
    b = list(set(a))
    print(b)
for i in b:
    result.append({i: a.count(i)})

result.sort(key=lambda x: x.values()[0], reverse=True)
print(result[:10])
