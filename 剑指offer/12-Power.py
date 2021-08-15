"""
给定一个double类型的浮点数base和int类型的整数exponent。求base的exponent次方。
保证base和exponent不同时为0
"""

# -*- coding:utf-8 -*-
class Solution:
    def q_power(self,b,n):
        if n == 0: return 1
        ret = self.q_power(b,n/2)
        if n&1:#奇数
            return ret * ret * b
        else:
            return ret * ret

    def Power(self, b, n):
        # write code here
        if n < 0:
            b = 1 / b
            n = -n
        return  self.q_power(b,n)