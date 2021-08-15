#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/6/12 12:05
# @Author  : lirixiang
# @Email   : 565539277@qq.com
# @File    : 19-stack.py
# -*- coding:utf-8 -*-
"""
定义栈的数据结构，请在该类型中实现一个能够得到栈中所含最小元素的min函数（时间复杂度应为O（1））。
注意：保证测试中不会当栈为空的时候，对栈调用pop()或者min()或者top()方法
"""
class Solution:
    def __init__(self):
        self.stack = []

    def push(self, node):
        # write code here
        self.stack.append(node)

    def pop(self):
        if self.stack:
            return self.stack.pop()
    # write code here
    def top(self):
    # write code here
        if self.stack:
            return self.stack[-1]
    def min(self):
    # write code here
        if self.stack:
            return self.stack[0]