#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/7/26 12:13
# @Author  : lirixiang
# @Email   : 565539277@qq.com
# @File    : 22-generateParenthesis.py
"""
数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。

 

示例：

输入：n = 3
输出：[
       "((()))",
       "(()())",
       "(())()",
       "()(())",
       "()()()"
     ]

"""
class Solution:
    def generateParenthesis(self, n: int):
        ans = []
        def backtrack(l, r, s):
            if l == 0 and r == 0:
                ans.append(s)
                return

            if l > 0:
                backtrack(l - 1, r, s + "(")
            if l < r and r > 0:
                backtrack(l, r - 1, s + ")")

        ans = []
        backtrack(n, n, '')
        return ans

s = Solution()
res = s.generateParenthesis(3)
print(res)