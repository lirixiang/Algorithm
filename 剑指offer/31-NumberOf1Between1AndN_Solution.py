#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/7/8 11:36
# @Author  : lirixiang
# @Email   : 565539277@qq.com
# @File    : 31-NumberOf1Between1AndN_Solution.py
"""
求出1~13的整数中1出现的次数,并算出100~1300的整数中1出现的次数？为此他特别
数了一下1~13中包含1的数字有1、10、11、12、13因此共出现6次,但是对于后面问
题他就没辙了。ACMer希望你们帮帮他,并把问题更加普遍化,
可以很快的求出任意非负整数区间中1出现的次数（从1 到 n 中1出现的次数）。
"""
# -*- coding:utf-8 -*-
class Solution:
    def NumberOf1Between1AndN_Solution(self, n):
     # write code here
        count = 0
        for i in range(0,n+1):
               while i > 0:
                   if i % 10 == 1:
                       count += 1
                       i = i/10
        return count
