#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random


a_list = range(30)
random.shuffle(a_list)
print a_list
# 使用选择排序对列表进行排序
for i in range(len(a_list) - 1):
    for j in range(i + 1, len(a_list)):
        if a_list[i] > a_list[j]:
            a_list[i], a_list[j] = a_list[j], a_list[i]

print a_list
