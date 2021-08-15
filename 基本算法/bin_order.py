#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/7/20 17:40
# @Author  : lirixiang
# @Email   : 565539277@qq.com
# @File    : bin_order.py

def post(root):
    stack = []
    node = root
    while stack or root:
        while node:
            stack.append(root)
            node = node.left if node.left else node.right
        node = stack.pop()
        if stack and stack[-1].left== root:
            root = stack[-1].left
        else:
            root = None

def postOrder(root):
    s1 = [root,]
    s2 = []
    while s1:
        node = s1.pop()
        s2.append(node)
        if node.left:s1.append(node.left)
        if node.right:s1.append(node.right)

    while s2:
        print(s2.pop().value)


def midOrder(root):
    stack = []
    node = root
    while node or stack:
        while node:
            stack.append(node)
            node = node.left
        node = stack.pop()
        print(node.val)
        node = node.right

def preOrder(root):
    stack = []
    node = root
    while node or stack:
        while node:
            print(node.val)
            stack.append(node)
            node = node.left
        node = stack.pop()
        node = node.right