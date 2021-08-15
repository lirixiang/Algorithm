#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/9/21 16:58
# @Author  : lirixiang
# @Email   : 565539277@qq.com
# @File    : pile.py
class Node():
    def __init__(self,val):
        self.val = val
        self.next = None

#1 3 2
#3 8 6
pHead1 = Node(1)
pHead1.next = Node(3)
pHead1.next.next = Node(3)

pHead2 = Node(3)
pHead2.next = Node(8)
pHead2.next.next = Node(6)
def merge(pHead1,pHead2):
    p1 = pHead1
    p2 = pHead2
    p3 = Node(-1)
    head = p3
    carry = 0
    while p1:

        while p2:

            value = p1.val + p2.val + carry
            carry = 0
            if value >= 10:
                carry = value // 10
                value = value % 10


            p3.next = Node(value)
            p2 = p2.next
            p3 = p3.next
            break
        p1 = p1.next
    return head.next


p = merge(pHead1,pHead2)
while p:
    print(p.val)
    p = p.next

