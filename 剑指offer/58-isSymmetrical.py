#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/7/17 15:48
# @Author  : lirixiang
# @Email   : 565539277@qq.com
# @File    : 58-isSymmetrical.py
"""
请实现一个函数，用来判断一棵二叉树是不是对称的。
注意，如果一个二叉树同此二叉树的镜像是同样的，定义其为对称的。
"""
# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def isSymmetrical(self, pRoot):
        # write code here
        if not pRoot:return True
        return self.dfs(pRoot.left,pRoot.right)


    def dfs(self,left,right):
        if not left and not right: return True
        if left != None and right != None:
            if left.val == right.val and self.dfs(left.left,right.right) and self.dfs(left.right,right.left):
                return True

        return False