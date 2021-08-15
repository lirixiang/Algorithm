"""
输入一个整数，输出该数二进制表示中1的个数。其中负数用补码表示。
"""
# -*- coding:utf-8 -*-
class Solution:
    def NumberOf1(self, n):
        # write code here
        ans = 0
        if n<0:n=n&0xffffffff
        while n != 0:
            ans += 1
            n = (n-1)&n
        return ans