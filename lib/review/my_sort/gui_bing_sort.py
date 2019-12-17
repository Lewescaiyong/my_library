#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random


def gui_bing_sort(one_list):
    """使用归并排序对列表进行排序
    Args:
        one_list        type(list)         一个乱序列表
    """

    def gui_bing(left, right):
        # 将两个有序列表合并成一个有序列表
        merge = list()
        while left and right:
            merge.append(left.pop(0) if left[0] < right[0] else right.pop(0))
        merge.extend(left or right)

        return merge

    if len(one_list) <= 1:
        return one_list

    mid = len(one_list) // 2
    l_list = gui_bing_sort(one_list[:mid])
    r_list = gui_bing_sort(one_list[mid:])
    result = gui_bing(l_list, r_list)

    return result


if __name__ == '__main__':
    a_list = range(30)
    random.shuffle(a_list)
    print a_list
    print gui_bing_sort(a_list)
