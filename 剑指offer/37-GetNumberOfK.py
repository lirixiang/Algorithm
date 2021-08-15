#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/7/13 14:01
# @Author  : lirixiang
# @Email   : 565539277@qq.com
# @File    : 37-GetNumberOfK.py
"""
统计一个数字在排序数组中出现的次数。
"""
# -*- coding:utf-8 -*-
class Solution:
    def GetNumberOfK(self, data, k):
        # write code here
        return data.count(k)
