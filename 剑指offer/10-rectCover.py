"""
题目描述
我们可以用2*1的小矩形横着或者竖着去覆盖更大的矩形。请问用n个2*1的小矩形无重叠地覆盖一个2*n的大矩形，总共有多少种方法？

比如n=3时，2*3的矩形块有3种覆盖方法：
https://uploadfiles.nowcoder.com/images/20200218/6384065_1581999858239_64E40A35BE277D7E7C87D4DCF588BE84
"""
# -*- coding:utf-8 -*-
class Solution:
    def rectCover(self, n):
        # write code here
        if n <= 2: return n
        num1 = 1
        num2 = 2
        for i in range(2,n+1):
            num1,num2 = num2,num1+num2
        return num1
