#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/7/1 18:16
# @Author  : lirixiang
# @Email   : 565539277@qq.com
# @File    : 21PrintFromTopToBottom.py
# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
"""
从上往下打印出二叉树的每个节点，同层节点从左至右打印。
"""
class Solution:
    # 返回从上到下每个节点值列表，例：[1,2,3]
    def PrintFromTopToBottom(self, root):
        # write code here
        if not root:
            return []
        q = [root,]
        res = []
        while q:
            node = q.pop(0)
            res.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

        return res

