#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/7/17 10:27
# @Author  : lirixiang
# @Email   : 565539277@qq.com
# @File    : 55-EntryNodeOfLoop.py
"""
题目描述
给一个链表，若其中包含环，请找出该链表的环的入口结点，否则，输出null。
"""


# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def EntryNodeOfLoop(self, pHead):
        # write code here
        slow,fast = pHead,pHead
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                break

        fast = pHead
        if fast == None or fast.next == None:
            return None

        while fast != slow:
            fast = fast.next
            slow = slow.next
        return slow
