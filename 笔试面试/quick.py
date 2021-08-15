#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/10/11 20:57
# @Author  : lirixiang
# @Email   : 565539277@qq.com
# @File    : quick.py
l = input()
i = 0
j = len(l)-1
def quick(l,i,j):
    if i >= j:
        return l

    mid = l[i]
    low = i
    high = j

    while i < j:
        while i < j and mid <= l[j]:
            j -= 1
        l[i] = l[j]

        while i < j and mid >= l[i]:
            i += 1
        l[j] = l[i]

    l[j] = mid

    quick(l,low,i-1)
    quick(l,i+1,high)
    return l

print(l)
l = [8,5,6,7,6,88,1,4]
l = quick(l,0,len(l)-1)
print(l)