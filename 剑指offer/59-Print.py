#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/7/17 16:47
# @Author  : lirixiang
# @Email   : 565539277@stackstack.com
# @File    : 59-Print.py
"""
请实现一个函数按照之字形打印二叉树，即第一行按照从左到右的顺序打印，
第二层按照从右至左的顺序打印，第三行按照从左到右的顺序打印，其他行以此类推。
"""
# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def Print(self, pRoot):
        # write code here
        if not pRoot: return []
        res = []
        q = [pRoot]
        level = 0
        while q:
            levelres = []
            for i in range(len(q)):
                node = q.pop(0)
                if level & 1 == 0:
                    levelres.append(node.val)
                else:
                    levelres.insert(0,node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(levelres)
            level += 1
        return res

        