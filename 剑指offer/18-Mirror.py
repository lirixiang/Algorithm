#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/6/8 4:19
# @Author  : lirixiang
# @Email   : 565539277@qq.com
# @File    : 18-Mirror.py
"""
操作给定的二叉树，将其变换为源二叉树的镜像
输入描述:
二叉树的镜像定义：源二叉树
    	    8
    	   /  \
    	  6   10
    	 / \  / \
    	5  7 9 11
    	镜像二叉树
    	    8
    	   /  \
    	  10   6
    	 / \  / \
    	11 9 7  5
"""

# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#方法一:递归
class Solution:
    # 返回镜像树的根节点
    def Mirror(self, root):
        # write code here
        if not root:return
        self.dfs(root)

    def dfs(self,r):
        if not r:return
        lval = self.dfs(r.left)
        rval = self.dfs(r.right)
        r.left,r.right = rval,lval
        return r

#方法二:层次遍历
import queue
class Solution:
    # 返回镜像树的根节点
    def Mirror(self, root):
        q = queue.Queue()
        q.put(root)
        while not q.empty():
            l = q.qsize()
            while l:
                l -= 1
                node = q.front()
                q.get()
                if node.left:q.put(node.left)
                if node.right:q.put(node.right)
                cur = node.left
                node.left = node.right
                node.right = cur