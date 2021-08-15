#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/7/6 15:17
# @Author  : lirixiang
# @Email   : 565539277@qq.com
# @File    : 26-Permutation.py
"""
题目描述
输入一个字符串,按字典序打印出该字符串中字符的所有排列。
例如输入字符串abc,则打印出由字符a,b,c所能排列出来的所有字符串abc,acb,bac,bca,cab和cba。
输入描述:
输入一个字符串,长度不超过9(可能有字符重复),字符只包括大小写字母。
"""

# -*- coding:utf-8 -*-
class Solution:
    def Permutation(self, ss):
        # write code here

        if len(ss) == 1 or len(ss) == 0:
            return ss

        sl = []
        for i in range(len(ss)):
            for j in self.Permutation(ss[:i]+ss[i+1:]):
                sl.append(ss[i] + j)

        sl = sorted(list(set(sl)))
        return sl




s =Solution()
sl = s.Permutation("aa")
print(sl)
