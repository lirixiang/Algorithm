"""
2.●给定一个正整数组a ,是否能以3个数为边长构成三角形?
●即是否存在不同的i,j,k,
●满足a[i] < a[j] + a[k]
●并且a[j]< a[i] + a[k]
●并且a[k]< a[i] + a[j]
"""
import collections

"""
1.设计一个队列
●支持:出队,入队,求最大元素
●要求0(1)
均摊分析
"""

"""
3.152 leetcode
"""

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        queue = collections.deque()
        queue.append(root)
        res = []
        while queue:
            size = len(queue)
            level = []
            for _ in range(size):
                cur = queue.popleft()
                if not cur:
                    continue
                level.append(cur.val)
                queue.append(cur.left)
                queue.append(cur.right)
            if level:
                res.append(level)

        return res

import pymysql
pymysql.connect