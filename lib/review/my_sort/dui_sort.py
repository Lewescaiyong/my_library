#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random


def heap_sort(one_list):
    """使用堆排序对列表进行排序
    Args:
        one_list         type(list)          需要进行堆排序的列表
    """
    # 将列表构造成堆
    list_to_heap(one_list, len(one_list))
    for i in range(len(one_list) - 1):
        # 交换根顶节点与末节点
        one_list[0], one_list[len(one_list) - 1 - i] = one_list[len(one_list) - 1 - i], one_list[0]
        # 将除末尾元素以外的元素构造成堆
        list_to_heap(one_list, len(one_list) - i - 1)


def list_to_heap(one_list, end=None, heap_type=0):
    """转换成堆
    Args:
        one_list         type(list)          需要转换成堆的列表
        end              type(int)           循环的节点个数
        heap_type        type(int)           堆类型, 0: 大根堆; 1: 小跟堆
    """
    node = end // 2

    if heap_type == 0:
        big_node_heap(one_list, node, end)
    else:
        less_node_heap(one_list, node, end)


def big_node_heap(one_list, node, end):
    """转换成大根堆
    Args:
        one_list         type(list)          需要转换成堆的列表
        node             type(int)           父节点个数
        end              type(int)           循环的节点个数
    """
    for i in range(0, node)[::-1]:
        while i < node:
            if (2 * i + 2) < end and one_list[2 * i + 1] < one_list[2 * i + 2]:
                one_list[2 * i + 1], one_list[2 * i + 2] = one_list[2 * i + 2], one_list[2 * i + 1]
            if one_list[i] < one_list[2 * i + 1]:
                one_list[i], one_list[2 * i + 1] = one_list[2 * i + 1], one_list[i]
            i += 1


def less_node_heap(one_list, node, end):
    """转换成小根堆
    Args:
        one_list         type(list)          需要转换成堆的列表
        node             type(int)           父节点个数
        end              type(int)           循环的节点个数
    """
    for i in range(0, node)[::-1]:
        while i < node:
            if (2 * i + 2) < end and one_list[2 * i + 1] > one_list[2 * i + 2]:
                one_list[2 * i + 1], one_list[2 * i + 2] = one_list[2 * i + 2], one_list[2 * i + 1]
            if one_list[i] > one_list[2 * i + 1]:
                one_list[i], one_list[2 * i + 1] = one_list[2 * i + 1], one_list[i]
            i += 1


if __name__ == '__main__':
    a_list = range(30)
    random.shuffle(a_list)
    print a_list
    heap_sort(a_list)
    print a_list
