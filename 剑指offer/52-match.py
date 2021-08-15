#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/7/16 11:47
# @Author  : lirixiang
# @Email   : 565539277@qq.com
# @File    : 52-match.py
"""
请实现一个函数用来匹配包括'.'和'*'的正则表达式。模式中的字符'.'表示任意一个字符，而'*'表示它前面的字符可以出现任意次（包含0次）。 在本题中，匹配是指字符串的所有字符匹配整个模式。
例如，字符串"aaa"与模式"a.a"和"ab*ac*a"匹配，但是与"aa.a"和"ab*a"均不匹配
"""
# -*- coding:utf-8 -*-
class Solution:
    # s, pattern都是字符串
    def match(self, s, pattern):
        # write code here
        if s == "" and pattern == "": return True
        pattern_str = ""
        for i in range(len(pattern)):
            if pattern[i] == "." and pattern[i + 1] == "*":
                if s == "": return True
                j = i
                while pattern[i + 2] != s[i]:
                    pattern_str += s[j]
                    j += 1
                continue
            if pattern[i] == "*" and pattern[i - 1] == "*":
                continue

            p = pattern[i]

            if s[i] == p:

                pattern_str += s[i]
                continue



            if p == ".":
                if s == "":
                    pattern_str += s
                else:
                    pattern_str += s[i]
                continue
            if p == "*":
                pattern_str = pattern_str[:-1]
                letter = pattern[i-1]
                j = i
                while letter == s[j+1]:
                    pattern_str += letter
                    j += 1
                continue
        if pattern_str == s:
            return True
        return False




