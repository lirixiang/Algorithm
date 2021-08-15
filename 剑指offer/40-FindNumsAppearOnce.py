#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/7/13 17:30
# @Author  : lirixiang
# @Email   : 565539277@qq.com
# @File    : 40-FindNumsAppearOnce.py
"""
一个整型数组里除了两个数字之外，其他的数字都出现了两次。请写程序找出这两个只出现一次的数字。
"""
# -*- coding:utf-8 -*-
class Solution:
    # 返回[a,b] 其中ab是出现一次的两个数字
    def FindNumsAppearOnce(self, array):
        # write code here
        noRepeatList = []
        for i in range(len(array)):
            if array[i] not in noRepeatList:
                noRepeatList.append(array[i])

        result = {}
        for i in range(len(noRepeatList)):
            count = 0
            for j in range(len(array)):
                if noRepeatList[i] == array[j]:
                    count += 1
            result[noRepeatList[i]] = count

        resList = []
        for i in result:
            if result[i] == 1:
                resList.append(i)
        return resList



