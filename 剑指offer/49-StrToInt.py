#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/7/15 14:57
# @Author  : lirixiang
# @Email   : 565539277@qq.com
# @File    : 49-StrToInt.py
"""
将一个字符串转换成一个整数，要求不能使用字符串转换整数的库函数。 数值为0或者字符串不是一个合法的数值则返回0
输入描述:
输入一个字符串,包括数字字母符号,可以为空
输出描述:
如果是合法的数值表达则返回该数字，否则返回0
示例1
输入
复制
+2147483647
1a33
输出
复制
2147483647
0
"""
import re
# -*- coding:utf-8 -*-
class Solution:
    def StrToInt(self, s):
        # write code here
        res = re.search(".*[\w]",s)
        return res

s = Solution()
res = s.StrToInt("er32r32@")
print(res)