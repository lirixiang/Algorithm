#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/9/13 12:21
# @Author  : lirixiang
# @Email   : 565539277@qq.com
# @File    : kmp.py
class Solution:
    def strStr(self,haystack,needle):
        def KMP(s,p):
            nex = getNext(p)
            i = 0
            j = 0
            while i < len(s) and j < len(p):
                if j == -1 or s[i] == p[j]:
                    i += 1
                    j += 1
                else:
                    j = nex[j]

            if j == len(p):
                return i - j
            else:
                return -1

        def getNext(p):
            nex = [0] * (len(p)+1)
            nex[0] = -1
            i = 0
            j = -1
            while i < len(p):
                if j == -1 or p[i] == p[j]:
                    i += 1
                    j += 1
                    nex[i] = j
                else:
                    j = nex[j]
            return nex

        KMP(haystack,needle)