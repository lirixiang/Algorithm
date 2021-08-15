#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/6/6 23:45
# @Author  : lirixiang
# @Email   : 565539277@qq.com
# @File    : 16-Merge.py
"""
输入两个单调递增的链表，输出两个链表合成后的链表，当然我们需要合成后的链表满足单调不减规则。
"""
# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        # write code here
        vHead = ListNode(-1)
        cur = vHead
        while pHead1 and pHead2:
            if pHead1.val < pHead2.val:
                cur.next = pHead1
                pHead1 = pHead1.next
            else:
                cur.next = pHead2
                pHead2 = pHead2.next
            cur = cur.next
        if  pHead1:
            cur.next = pHead1
        else:
            cur.next = pHead2
        return vHead.next