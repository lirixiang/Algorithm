#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/6/6 22:40
# @Author  : lirixiang
# @Email   : 565539277@qq.com
# @File    : 14-FindKthToTail.py
"""
输入一个链表，输出该链表中倒数第k个结点。
"""
# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

#解法一:普通解法
class Solution1:
    def FindKthToTail(self, head, k):
        # write code here
        if head==None or k <= 0:return None
        cur = head
        n = 0
        while cur:
            cur = cur.next
            n += 1

        if n < k:return None
        n -= k
        while n:
            head = head.next
            n -= 1
        return head

#解法二:快慢指针
class Solution2:
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


