#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random


class Node(object):
    """树节点类
    """

    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None


class BST(object):
    """二叉查找树
    """

    def __init__(self, node_list):
        self.root = Node(node_list[0])
        for i in node_list[1:]:
            self.insert(i)

    def search(self, node, parent, value):
        """查找二叉树中的子节点
        Args:
            node         type(Node)         查询起始节点对象
            parent       type(Node)         node的父节点对象
            value        type(int, str...)  需要查找的子节点的value属性值
        """
        if node is None:
            return False, node, parent
        if node.value == value:
            return True, node, parent
        if node.value > value:
            return self.search(node.left_child, node, value)

        return self.search(node.right_child, node, value)

    def insert(self, value):
        """往二叉树中插入子节点
        Args:
            value        type(int, str...)        需要插入的子节点的value属性值
        """
        flag, node, parent = self.search(self.root, self.root, value)
        if not flag:
            node = Node(value)
            if value > parent.value:
                parent.right_child = node
            else:
                parent.left_child = node

    def delete(self, value):
        """删除二叉树中的子节点
        Args:
            value        type(int, str...)        需要删除的子节点的value属性值
        """
        flag, node, parent = self.search(self.root, self.root, value)
        if not flag:
            print 'Not find node by value: %s' % value
            return
        if node.left_child is None or node.right_child is None:
            if node == parent.left_child:
                parent.left_child = node.left_child or node.right_child
            else:
                parent.right_child = node.left_child or node.right_child
        else:
            next_child = node.right_child
            if next_child.left_child is None:
                node.value = next_child.value
                node.right_child = next_child.right_child
            else:
                next_parent = None
                while next_child.left_child is not None:
                    next_parent = next_child
                    next_child = next_child.left_child
                node.value = next_child.value
                next_parent.left_child = next_child.right_child

    def pre_order_traversal(self, node):
        """先序遍历
        Args:
            node        type(Node)        需要遍历的起始节点对象
        """
        if node is not None:
            print node.value
            self.pre_order_traversal(node.left_child)
            self.pre_order_traversal(node.right_child)

    def in_order_traversal(self, node):
        """中序遍历
        Args:
            node        type(Node)        需要遍历的起始节点对象
        """
        if node is not None:
            self.pre_order_traversal(node.left_child)
            print node.value
            self.pre_order_traversal(node.right_child)

    def post_order_traversal(self, node):
        """后序遍历
        Args:
            node        type(Node)        需要遍历的起始节点对象
        """
        if node is not None:
            self.pre_order_traversal(node.left_child)
            self.pre_order_traversal(node.right_child)
            print node.value


if __name__ == '__main__':
    a_list = range(30)
    random.shuffle(a_list)
    print a_list
    bst = BST(a_list)
    f, n, p = bst.search(bst.root, bst.root, 20)
    print 'node.value:', n.value
    bst.pre_order_traversal(bst.root)
