#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/7/17 10:52
# @Author  : lirixiang
# @Email   : 565539277@qq.com
# @File    : 56- deleteDuplication.py
"""
在一个排序的链表中，存在重复的结点，请删除该链表中重复的结点，
重复的结点不保留，返回链表头指针。 例如，链表1->2->3->3->4->4->5 处理后为 1->2->5
"""
# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def deleteDuplication(self, pHead):
        # write code here
        vHead = ListNode(-1)
        vHead.next = pHead
        pre = vHead
        cur = vHead
        while cur:
            cur = cur.next
            while cur and cur.next and cur.val == cur.next.val:
                t = cur.next.val
                while cur and t == cur.val:
                    cur = cur.next
                pre.next = cur
        return pHead