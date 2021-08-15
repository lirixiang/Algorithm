#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/10/18 16:05
# @Author  : lirixiang
# @Email   : 565539277@qq.com
# @File    : maxValue.py
class Solution:
    def maxValue(self,matrix):
        row =len(matrix)
        col =len(matrix[0])
        for i in range(row):
            for j in range(col):
                if i == j == 0:
                    continue
                elif i == 0:
                    matrix[i][j] = matrix[i][j-1] + matrix[i][j]
                elif j == 0:
                    matrix[i][j] = matrix[i-1][j] + matrix[i][j]
                else:
                    matrix[i][j] = max(matrix[i-1][j],matrix[i][j-1]) + matrix[i][j]
        return matrix[-1][-1]