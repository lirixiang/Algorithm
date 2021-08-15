#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/7/13 13:08
# @Author  : lirixiang
# @Email   : 565539277@qq.com
# @File    : 36 - FindFirstCommonNode.py
"""
输入两个链表，找出它们的第一个公共结点。
（注意因为传入数据是链表，所以错误测试数据的提示是用其他方式显示的，保证传入数据是正确的）
"""


# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    def FindFirstCommonNode(self, pHead1, pHead2):
        if pHead1 == None or pHead2 == None:
            return None
        # write code here
        p1 = pHead1
        p2 = pHead2
        while p1 != p2:
            if p1 != None: p1 = p1.next
            if p2 != None: p2 = p2.next
            if p1 != p2:
                if p1 == None:p1 = pHead2
                if p2 == None:p2 = pHead1
        return p1


