#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/7/8 17:50
# @Author  : lirixiang
# @Email   : 565539277@qq.com
# @File    : 33-GetUglyNumber_Solution.py
"""
把只包含质因子2、3和5的数称作丑数（Ugly Number）。例如6、8都是丑数，但14不是，
因为它包含质因子7。 习惯上我们把1当做是第一个丑数。求按从小到大的顺序的第N个丑数。
"""
# -*- coding:utf-8 -*-
class Solution:
    def GetUglyNumber_Solution(self, index):
        # write code here
        p1 = 0
        p2 = 0
        p3 = 0
        uglyList = [1]
        for i in range(1,index+1):
            ugly = min(uglyList[p1] * 2,uglyList[p2] * 3,uglyList[p3] * 3)
            uglyList.append(ugly)
            if ugly % 2 == 0:
                p1 += 1
            if ugly % 3 == 0:
                p2 += 1
            if ugly % 5 == 0:
                p3 += 1
        return uglyList[-1]





s =Solution()
res = s.GetUglyNumber_Solution(25)
#1 2 3 5 6 8 9 12 16 18 20
#1 2 3 4 5 6 7 8 9 10
print(res)