#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/7/2 15:41
# @Author  : lirixiang
# @Email   : 565539277@qq.com
# @File    : 23FindPath.py
# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

"""
输入一颗二叉树的根节点和一个整数，按字典序打印出二叉树中结点值的和为输入整数的所有路径。
路径定义为从树的根结点开始往下一直到叶结点所经过的结点形成一条路径。
"""
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # 返回二维列表，内部每个列表表示找到的路径
    def FindPath(self, root, expectNumber):
        # write code here
        if root == None:
            return []
        def DFS(root, path):
            if root.left == None and root.right == None and sum(path) == expectNumber:
                result.append(path)
            if root.left != None:
                DFS(root.left,  path+[root.left.val])
            if root.right != None:
                DFS(root.right,  path+[root.right.val])
        result = []
        DFS(root, [root.val])
        return result
