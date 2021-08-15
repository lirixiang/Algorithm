#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/7/13 15:07
# @Author  : lirixiang
# @Email   : 565539277@qq.com
# @File    : 39-IsBalanced_Solution.py
"""
输入一棵二叉树，判断该二叉树是否是平衡二叉树。

在这里，我们只需要考虑其平衡性，不需要考虑其是不是排序二叉树
"""
# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def __init__(self):
        self.isBalanced = True

    def IsBalanced_Solution(self, pRoot):
        # write code here
        self.maxDepth(pRoot)
        return self.isBalanced

    def maxDepth(self,pRoot):
        if not pRoot:
            return 0
        if not self.isBalanced: return 1
        left = self.maxDepth(pRoot.left) + 1
        right = self.maxDepth(pRoot.right) + 1
        if abs(left - right) > 1:
            self.isBalanced = False
        return max(left,right)
