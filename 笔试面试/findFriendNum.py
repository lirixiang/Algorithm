#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/10/21 21:44
# @Author  : lirixiang
# @Email   : 565539277@qq.com
# @File    : findFriendNum.py
class Solution:
    def findFriendNum(self, M):
        def dfs(x, y, n, m):
            if not (0 <= x < n and 0 <= y < m) or M[x][y] != 1:
                return
            M[x][y] = '2'
            dfs(x - 1, y, n, m)
            dfs(x + 1, y, n, m)
            dfs(x, y - 1, n, m)
            dfs(x, y + 1, n, m)

        if len(M) == 0 or len(M[0]) == 0:
            return 0
        res = 0
        n = len(M)
        m = len(M[0])
        for i in range(n):
            for j in range(m):
                if M[i][j] != 1:
                    continue
                dfs(i, j, n, m)
                res += 1
        return res

