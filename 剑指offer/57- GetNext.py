#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/7/17 11:50
# @Author  : lirixiang
# @Email   : 565539277@qq.com
# @File    : 57- GetNext.py
"""
给定一个二叉树和其中的一个结点，请找出中序遍历顺序的下一个结点并且返回。
注意，树中的结点不仅包含左右子结点，同时包含指向父结点的指针。
"""

# -*- coding:utf-8 -*-
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None
class Solution:
    def GetNext(self, pNode):
        # write code here

        tmp = pNode
        while tmp.next:
            tmp = tmp.next

        self.v = []
        self.midOrder(tmp)
        if self.v.index(pNode) != len(self.v) - 1:
            return self.v[self.v.index(pNode) + 1]
        else:
            return None



    def midOrder(self,root):
        if not root:
            return

        self.midOrder(root.left)
        self.v.append(root)
        self.midOrder(root.right)