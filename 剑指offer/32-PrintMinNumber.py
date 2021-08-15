#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/7/8 16:20
# @Author  : lirixiang
# @Email   : 565539277@qq.com
# @File    : 32-PrintMinNumber.py
"""
输入一个正整数数组，把数组里所有数字拼接起来排成一个数，打印能拼接出的所有数字中最小的一个。
例如输入数组{3，32，321}，则打印出这三个数字能排成的最小数字为321323。
"""
# -*- coding:utf-8 -*-
class Solution:
    def PrintMinNumber(self, numbers) -> str:
        # write code here

        if len(numbers) == 0:
            return ""
        res = list(map(int, self.Permutation(numbers)))

        def bubble_sort(arr):
            n = len(arr)
            for i in range(n):
                for j in range(n - 1 - i):
                    if arr[j] > arr[j + 1]:
                        arr[j], arr[j + 1] = arr[j + 1], arr[j]
            return arr

        arr = bubble_sort(res)
        return arr[0]

    def Permutation(self, numbers):
        if len(numbers) == 1:
            return numbers

        str_numbers = list(map(str, numbers))
        sl = []
        for i in range(len(str_numbers)):
            for j in self.Permutation(str_numbers[:i] + str_numbers[i + 1:]):
                sl.append(str_numbers[i] + j)
        return sl


s = Solution()
res = s.PrintMinNumber([3,32,321])
print(res)