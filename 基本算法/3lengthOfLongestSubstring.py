# 给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:return 0
        left = 0
        lookup = set()
        max_len = 0
        cur_len = 0
        for i in range(len(s)):
            cur_len += 1
            # print(cur_len)
            while s[i] in lookup:
                lookup.remove(s[left])
                left += 1
                print(left)
                cur_len -= 1
                # print(cur_len)
            # if cur_len > max_len:
            #     max_len = cur_len
            lookup.add(s[i])
        print(cur_len)
        print(max_len)
        return max_len
Solution().lengthOfLongestSubstring("sadfwefwe")