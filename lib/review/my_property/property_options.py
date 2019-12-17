#!/usr/bin/env python
# -*- coding: utf-8 -*-


class MyProperty(object):
    """复习特性"""

    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        """定义name属性的获取"""

        return self.__name

    @name.setter
    def name(self, value):
        """定义name属性的修改"""

        self.__name = value

    @name.deleter
    def name(self):
        """定义name属性的删除"""

        del self.__name

print MyProperty.__module__