#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/9/12 23:27
# @Author  : lirixiang
# @Email   : 565539277@qq.com
# @File    : removeInvalidParetheses.py
class Solution:
    def removeInvalidParentheses(self, s: str):

        def isvalid(string):
            l = 0
            for c in string:
                if c == "(":
                    l += 1
                elif c == ")":
                    l -= 1
                    if l < 0:
                        return False
            if l == 0: return True

        level = {s}
        while True:
            valid = list(filter(isvalid, level))
            if valid:
                return valid
            for i in range(len(s)):
                for c in level:
                    if c[i] in "()":
                        level = {c[:i] + c[i + 1:]}



s = Solution()
s.removeInvalidParentheses("()())()")
