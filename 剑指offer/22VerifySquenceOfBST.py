#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/7/1 18:50
# @Author  : lirixiang
# @Email   : 565539277@qq.com
# @File    : 22VerifySquenceOfBST.py
"""
输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历的结果。
如果是则输出Yes,否则输出No。假设输入的数组的任意两个数字都互不相同。
"""
# -*- coding:utf-8 -*-
class Solution:
    def VerifySquenceOfBST(self, sequence):
        # write code here
        if len(sequence) == 0:
            return False
        return  self.subVerifySquenceOfBST(sequence)

    def subVerifySquenceOfBST(self,sequence):
        if len(sequence) <= 2:
            return True
        root = sequence[-1]
        i = 0
        while True:
            if root > sequence[i]:
                i += 1
            else:
                break

        j = i
        while j < len(sequence) - 1:
            if root < sequence[j]:
                j += 1
            else:
                return False

        return self.subVerifySquenceOfBST(sequence[:i]) and self.subVerifySquenceOfBST(sequence[i:-1])


