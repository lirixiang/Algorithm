"""
在一个二维数组中（每个一维数组的长度相同），每一行都按照从左到右递增的顺序排序，
每一列都按照从上到下递增的顺序排序。请完成一个函数，输入这样的一个二维数组和一个整数，
判断数组中是否含有该整数。
"""

# -*- coding:utf-8 -*-
class Solution:
    # array 二维列表

    def Find(self, target, array):
        # write code here
        m = len(array)
        if m == 0: return False
        n = len(array[0])
        if n == 0: return False
        r = 0
        c = n - 1
        while r < m and c > 0:
            if target == array[r][c]:
                return True
            elif target > array[r][c]:
                r+=1
            else:
                c-=1
        return False




if __name__ == '__main__':
    array = [[1,2,3],[4,5,6],[7,8,9],[10,11,12]]
    s = Solution()
    print(s.Find(9,array))