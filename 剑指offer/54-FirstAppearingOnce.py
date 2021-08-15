#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/7/16 18:05
# @Author  : lirixiang
# @Email   : 565539277@qq.com
# @File    : 54-FirstAppearingOnce.py
"""
请实现一个函数用来找出字符流中第一个只出现一次的字符。
例如，当从字符流中只读出前两个字符"go"时，第一个只出现一次的字符是"g"。
当从该字符流中读出前六个字符“google"时，第一个只出现一次的字符是"l"。
输出描述:
如果当前字符流没有存在出现一次的字符，返回#字符。
"""
# -*- coding:utf-8 -*-
class Solution:
    # 返回对应char
    def __init__(self):
        self.s = ""
    def FirstAppearingOnce(self):
        # write code here
        hashList = [0] * 256
        for i in self.s:
            hashList[ord(i)] += 1


        for j in str(self.s):
            if hashList[ord(j)] == 1:
                return j
        return "#"
    def Insert(self, char):
        # write code here
        self.s += char


s =Solution()
for i in "google":
    s.Insert(i)
    s.FirstAppearingOnce()


