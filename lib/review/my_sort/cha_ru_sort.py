#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random


a_list = range(30)
random.shuffle(a_list)
print a_list
# 使用插入排序对列表进行排序
for i in range(1, len(a_list)):
    current = i
    while (a_list[current] < a_list[current - 1]) and current > 0:
        a_list[current], a_list[current - 1] = a_list[current - 1], a_list[current]
        current -= 1

print a_list