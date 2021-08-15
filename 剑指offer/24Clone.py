#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/7/3 16:35
# @Author  : lirixiang
# @Email   : 565539277@qq.com
# @File    : 24Clone.py
"""
输入一个复杂链表（每个节点中有节点值，以及两个指针，一个指向下一个节点，
另一个特殊指针random指向一个随机节点），请对此链表进行深拷贝，并返回拷贝后的头结点。
（注意，输出结果中请不要返回参数中的节点引用，否则判题程序会直接返回空）
"""

# -*- coding:utf-8 -*-
class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None
class Solution:
    # 返回 RandomListNode
    def Clone(self, pHead):
        if pHead == None:
            return None
        # write code here
        newhead = RandomListNode(pHead.label)
        newhead.next = pHead.next
        newhead.random = pHead.random
        newhead.next = self.Clone(pHead.next)
        return newhead


