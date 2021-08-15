#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/6/8 3:29
# @Author  : lirixiang
# @Email   : 565539277@qq.com
# @File    : 17-HasSubtree.py
# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

"""
输入两棵二叉树A，B，判断B是不是A的子结构。（ps：我们约定空树不是任意一个树的子结构）
"""

# 方法：递归求解
class Solution:
    def dfs(self,r1,r2):
        if not r1:return False
        if not r2:return True
        return r1.val == r2.val and self.dfs(r1.left,r2.left) and self.dfs(r1.right,r2.right)

    def HasSubtree(self, pRoot1, pRoot2):
        # write code here
        if not pRoot1 or not pRoot2:return False
        return self.dfs(pRoot1,pRoot2) or self.HasSubtree(pRoot1.left,pRoot2) or self.HasSubtree(pRoot1.right,pRoot2)