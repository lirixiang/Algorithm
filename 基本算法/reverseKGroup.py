#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/7/20 18:11
# @Author  : lirixiang
# @Email   : 565539277@qq.com
# @File    : reverseKGroup.py
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseKGroup(self, head, k):
        h = ListNode(-1)
        h.next = head
        pre = h
        cur = h

        n = -1
        while cur != None:
            n += 1
            cur = cur.next

        while n >= k:
            cur = pre.next
            for _ in range(k - 1):
                lat = cur.next
                cur.next = lat.next
                lat.next = pre.next
                pre.next = lat
            pre = cur
            n -= k
        return h.next

