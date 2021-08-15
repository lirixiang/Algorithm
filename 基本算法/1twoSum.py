nums = [2, 7, 11, 15]
target = 9


class Solution:

    def twoSum(self, nums,target):
        dict = {}
        for i,j in enumerate(nums):
            other_nums = target -nums[i]
            if dict.get(other_nums) != None:
                return [dict.get(other_nums) , i]
            else:
                dict[nums[i]] = i
        return None

s= Solution()
print(s.twoSum(nums,target))