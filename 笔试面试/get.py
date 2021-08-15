#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/10/11 20:40
# @Author  : lirixiang
# @Email   : 565539277@qq.com
# @File    : get.py
class Solution:
    def get(self,s):
        import collections
        map = collections.OrderedDict()
        for i in range(1,len(s)):
            bucket = s[i] + s[i-1]
            if bucket not in map:
                map[bucket] = 1
            else:
                map[bucket] += 1
        print(map)
        _max = 0
        for i in map:
            if map[i] > _max:
                _max = map[i]
        res = []
        for i in map:
            if map[i] == _max:
                res.append(i)

        return res
s = Solution()
l = s.get("abacadabad")
print(l)
