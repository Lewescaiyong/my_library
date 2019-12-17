#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random


def shun_xu_find(one_list, value):
    """使用顺序查找算法查找列表元素
    Args:
        one_list        type(list)         一个乱序列表
        value           type(int, str...)  查找的元素
    """
    for i, v in enumerate(one_list):
        if v == value:
            return i

    return -1


if __name__ == '__main__':
    a_list = range(30)
    random.shuffle(a_list)
    print a_list
    print shun_xu_find(a_list, 25)
