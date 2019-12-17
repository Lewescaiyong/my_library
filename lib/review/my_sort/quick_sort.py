#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random


def quick_sort(one_list, start=0, end=None):
    """使用快速排序对列表进行排序
    Args:
        one_list        type(list)         一个乱序列表
        start           type(int)          列表的起始索引
        end             type(int)          列表的末尾索引
    """
    if end is None:
        end = len(one_list) - 1
    if start < end:
        i, j = start, end
        base = one_list[i]
        # 将one_list分割成两个列表
        while i < j:
            # 在右侧寻找一个比base小的元素
            while i < j and one_list[j] >= base:
                j -= 1
            one_list[i] = one_list[j]
            # 在左侧侧寻找一个比base大的元素
            while i < j and one_list[i] <= base:
                i += 1
            one_list[j] = one_list[i]
        one_list[i] = base
        # 分别对两个列表进行递归
        quick_sort(one_list, start, i - 1)
        quick_sort(one_list, j + 1, end)


if __name__ == '__main__':
    a_list = range(30)
    random.shuffle(a_list)
    print a_list
    quick_sort(a_list)
    print a_list
