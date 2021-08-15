#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/7/18 14:04
# @Author  : lirixiang
# @Email   : 565539277@qq.com
# @File    : 64-maxInWindows.py
"""
给定一个数组和滑动窗口的大小，找出所有滑动窗口里数值的最大值。例如，如
果输入数组{2,3,4,2,6,2,5,1}及滑动窗口的大小3，那么一共存在6个滑动窗口，他
们的最大值分别为{4,4,6,6,6,5}； 针对数组{2,3,4,2,6,2,5,1}的滑动窗口有以下
6个： {[2,3,4],2,6,2,5,1}， {2,[3,4,2],6,2,5,1}， {2,3,[4,2,6],2,5,1}，
 {2,3,4,[2,6,2],5,1}， {2,3,4,2,[6,2,5],1}， {2,3,4,2,6,[2,5,1]}。
"""
# -*- coding:utf-8 -*-
class Solution:
    def maxInWindows(self, num, size):
        # write code here

        res = []
        for i in range(len(num)-size + 1):
            p = i
            q = i + size
            maxNum = 0
            for j in range(p,q):
                sub = num[p:q]
                maxNum = max(sub)
            res.append(maxNum)
        return res

s = Solution()
res = s.maxInWindows([2,3,4,2,6,2,5,1],3)
print(res)