#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/7/27 12:13
# @Author  : lirixiang
# @Email   : 565539277@qq.com
# @File    : topk.py
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        size = len(nums)

        def maxheap(i):
            l = 2 * i + 1
            r = 2 * i + 2
            large = i
            if l < size and nums[l] > nums[large]:
                large = l
            if r < size and nums[r] > nums[large]:
                large = r
            if large != i:
                nums[large], nums[i] = nums[i], nums[large]
                maxheap(large)

        for i in range(size // 2 - 1, -1, -1):
            maxheap(i)

        for i in range(size - 1, size - k, -1):
            nums[0], nums[i] = nums[i], nums[0]
            size -= 1
            maxheap(0)
        print(nums)
        return nums[0]



