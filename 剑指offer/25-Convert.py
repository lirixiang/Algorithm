#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/7/3 17:54
# @Author  : lirixiang
# @Email   : 565539277@qq.com
# @File    : 25-Convert.py
"""
输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的双向链表。
要求不能创建任何新的结点，只能调整树中结点指针的指向。
"""

# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.listHead = None
        self.listTail = None
    def Convert(self, pRootOfTree):
        # write code here
        if pRootOfTree == None:
            return None

        self.Convert(pRootOfTree.left)

        if self.listHead == None:
            self.listHead = pRootOfTree
            self.listTail = pRootOfTree
        else:
            self.listTail.right = pRootOfTree
            pRootOfTree.left = self.listTail
            self.listTail = pRootOfTree
        self.Convert(pRootOfTree.right)
        return self.listHead