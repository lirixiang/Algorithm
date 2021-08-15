#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/7/17 17:58
# @Author  : lirixiang
# @Email   : 565539277@qq.com
# @File    : 60-Print2.py
class Solution:
    def Print(self, pRoot):
        # write code here
        if not pRoot: return []
        res = []
        q = [pRoot]

        while q:
            levelres = []
            for i in range(len(q)):
                node = q.pop(0)

                levelres.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(levelres)

        return res