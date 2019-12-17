#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random


a_list = range(30)
random.shuffle(a_list)
print a_list
# 使用冒泡排序对列表进行排序
is_sort = False
for i in range(1, len(a_list)):
    for j in range(0, len(a_list) - i):
        if a_list[j] > a_list[j + 1]:
            a_list[j], a_list[j + 1] = a_list[j + 1], a_list[j]
            is_sort = True
    if not is_sort:
        break

print a_list
