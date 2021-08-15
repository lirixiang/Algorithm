#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/7/18 12:56
# @Author  : lirixiang
# @Email   : 565539277@qq.com
# @File    : 62-KthNode.py
"""
给定一棵二叉搜索树，请找出其中的第k小的结点。例如， （5，3，7，2，4，6，8）    中，
按结点数值大小顺序第三小结点的值为4。
"""
# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回对应节点TreeNode
    def KthNode(self, pRoot, k):
        # write code here
        if not pRoot or not k:return
        self.res = []
        self.midOrder(pRoot)
        if k <= len(self.res):
            return self.res[k-1]
        else:
            return None

    def midOrder(self,root):
        if not root:return
        self.midOrder(root.left)
        self.res.append(root)
        self.midOrder(root.right)
