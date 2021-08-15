#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/7/15 14:56
# @Author  : lirixiang
# @Email   : 565539277@qq.com
# @File    : 48-Add.py
"""
写一个函数，求两个整数之和，要求在函数体内不得使用+、-、*、/四则运算符号。
"""
# -*- coding:utf-8 -*-
class Solution:
    def Add(self, num1, num2):
        # write code here
        while num2:

            num1 =( num1 ^ num2) & 0xFFFFFFFF
            num2 =  ((num1 & num2) <<1)  & 0xFFFFFFFF
        return num1 if num1<=0x7FFFFFFF else ~(num1^0xFFFFFFFF)