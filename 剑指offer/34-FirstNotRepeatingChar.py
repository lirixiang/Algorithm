#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/7/9 13:06
# @Author  : lirixiang
# @Email   : 565539277@qq.com
# @File    : 34-FirstNotRepeatingChar.py
"""

在一个字符串(0<=字符串长度<=10000，全部由字母组成)中找到第一个只出现一次的字符,
并返回它的位置, 如果没有则返回 -1（需要区分大小写）.（从0开始计数）
"""
class Solution:
    def FirstNotRepeatingChar(self, s):
        # write code here
        ls=[0]*128

        for i in s:

            ls[ord(i)] += 1

        for j in s:
            if ls[ord(j)] == 1:
                return s.index(j)
        return -1



s = Solution()
res = s.FirstNotRepeatingChar("NXWtnzyoHoBhUJaPauJaAitLWNMlkKwDYbbigdMMaYfkVPhGZcrEwp")
print(res)
