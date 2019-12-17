#!/usr/bin/env python
# -*- coding: utf-8 -*-


def er_fen_find(one_list, value, start=0, end=None):
    """使用二分查找算法查找列表元素
    Args:
        one_list        type(list)         一个乱序列表
        value           type(int, str...)  查找的元素
        start           type(int)          查找的起始索引
        end             type(int)          查找的末尾索引
    """
    if end is None:
        end = len(one_list) - 1
    if start > end:
        return -1
    mid = (start + end) // 2
    if value < one_list[mid]:
        return er_fen_find(one_list, value, start, mid - 1)
    if value > one_list[mid]:
        return er_fen_find(one_list, value, mid + 1, end)

    return mid


if __name__ == '__main__':
    a_list = range(0, 30, 2)
    print a_list
    print er_fen_find(a_list, 10)
