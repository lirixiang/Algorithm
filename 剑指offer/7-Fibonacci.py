"""
大家都知道斐波那契数列，现在要求输入一个整数n，请你输出斐波那契数列的第n项（从0开始，第0项为0，第1项是1）。
n<=39
"""


# -*- coding:utf-8 -*-
class Solution:
    def Fibonacci(self, n):
        num1 = 0
        num2 = 1

        for i in range(1, n + 1):
            num1, num2 = num2, num1 + num2

        return num1
