"""
    :type prices: List[int]
    :rtype: int
"""
class Solution:
    def maxProfit(self, prices):
        max = 0
        min = 100000
        for i in range(len(prices)):
            if prices[i] < min:
                min = prices[i]
            if prices[i] - min > max:
                max = prices[i] - min
        return  max

s = Solution()
a = s.maxProfit([2,3,4,5,6])
print(a)
