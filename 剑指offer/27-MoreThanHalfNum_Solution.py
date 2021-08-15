#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/7/6 16:09
# @Author  : lirixiang
# @Email   : 565539277@qq.com
# @File    : 27-MoreThanHalfNum_Solution.py
"""
数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。
例如输入一个长度为9的数组{1,2,3,2,2,2,5,4,2}。
由于数字2在数组中出现了5次，超过数组长度的一半，因此输出2。如果不存在则输出0。
"""
# -*- coding:utf-8 -*-
class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        count = 0
        numbers.sort()
        res = numbers[len(numbers)/2]
        for i in numbers:
            if i == res:
                count +=1
        if count >len(numbers)/2:
            return res
        else:
            return 0

