#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/7/9 15:26
# @Author  : lirixiang
# @Email   : 565539277@qq.com
# @File    : 35-InversePairs.py
"""
题目描述
在数组中的两个数字，如果前面一个数字大于后面的数字，
则这两个数字组成一个逆序对。输入一个数组,求出这个数组中的逆序对的总数P。
并将P对1000000007取模的结果输出。 即输出P%1000000007
输入描述:
题目保证输入的数组中没有的相同的数字

数据范围：
	对于%50的数据,size<=10^4
	对于%75的数据,size<=10^5
	对于%100的数据,size<=2*10^5

示例1
输入
1,2,3,4,5,6,7,0

输出
7
"""
# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.count = 0

    def InversePairs(self, data):
        # write code here
        if len(data) < 2:return 0
        self.mergeSort(data)
        return self.count % 1000000007

    def mergeSort(self,data):
        if len(data) < 2:return data
        mid = len(data) // 2
        left = self.mergeSort(data[:mid])

        right = self.mergeSort(data[mid:])

        i,j = 0,0
        merged = []
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                merged.append(left[i])

                i += 1
            else:
                merged.append(right[j])
                j += 1
                self.count += (len(left) - i)

        return merged + left[i:] + right[j:]






s =Solution()
res = s.InversePairs([3,6,4,0,7,9,2,1,5])

