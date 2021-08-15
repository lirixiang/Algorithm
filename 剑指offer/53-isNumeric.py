#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/7/16 17:26
# @Author  : lirixiang
# @Email   : 565539277@qq.com
# @File    : 53-isNumeric.py
"""
请实现一个函数用来判断字符串是否表示数值（包括整数和小数）。
例如，字符串"+100","5e2","-123","3.1416"和"-1E-16"都表示数值。
但是"12e","1a3.14","1.2.3","+-5"和"12e+4.3"都不是。
"""
# -*- coding:utf-8 -*-
class Solution:
    # s字符串
    def isNumeric(self, s):
        # write code here
        label = ["+","-"]
        numList = ["0","1","2","3","4","5","6","7","8","9"]
        for i in range(len(s)):
            if s[0] in label:
                continue
            if s[i] not in numList:
                if s[i] == "e" or s[i] == "E":
                    continue
                return False
