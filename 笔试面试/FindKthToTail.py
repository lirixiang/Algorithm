#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/10/21 20:11
# @Author  : lirixiang
# @Email   : 565539277@qq.com
# @File    : FindKthToTail.py

class ListNode():
    def __init__(self,val,next=None):
        self.val = val
        self.next = next

class Solution:
    def FindKthToTail(self, head, k):
        if not head or k <= 0:return None
        slow,fast = head,head
        while k:
            k -= 1
            if fast:
                fast = fast.next
            else:
                return None

        while fast:
            slow = slow.next
            fast = fast.next
        return slow
