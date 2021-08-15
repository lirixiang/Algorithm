#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/7/18 14:07
# @Author  : lirixiang
# @Email   : 565539277@qq.com
# @File    : 67-cutRope.py
"""
给你一根长度为n的绳子，请把绳子剪成整数长的m段（m、n都是整数，n>1并且m>1，m<=n），每段绳子的长度记为k[1],...,k[m]。请问k[1]x...xk[m]可能的最大乘积是多少？例如，当绳子的长度是8时，我们把它剪成长度分别为2、3、3的三段，此时得到的最大乘积是18。
输入描述:
输入一个数n，意义见题面。（2 <= n <= 60）
输出描述:
输出答案。
示例1
输入
8
输出
18
"""


class Solution:
    def cutRope(self, number):
        # write code here

        # 申请辅助空间
        # products = [0]*(number+1)
        # 定义前几个初始变量的值
        products = [0] * (number + 1)
        products[0] = 0
        products[1] = 1
        products[2] = 2
        products[3] = 3
        # 进行动态规划,也就是从下向上的进行求解
        for i in range(4, number + 1):
            dp = 0
            for j in range(1, i):
                dp = max(products[j] * products[i - j], dp)
            products[i] = dp

        return products[number]