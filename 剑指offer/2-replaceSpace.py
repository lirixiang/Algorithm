"""
请实现一个函数，将一个字符串中的每个空格替换成“%20”。
例如，当字符串为We Are Happy.则经过替换之后的字符串为We%20Are%20Happy。
"""
# -*- coding:utf-8 -*-
class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        # write code here
        if s == "" or not isinstance(s,str) or s == None or len(s)<0:return False
        cnt = 0 # 空格的个数
        for i in s:
            if i == ' ':cnt+=1

        new_length = len(s) + cnt*2
        new_str = new_length * [None]
        indexOfOriginal = len(s) - 1
        indexOfNew = new_length - 1

        while indexOfNew >= 0 and indexOfOriginal <= indexOfNew:
           if s[indexOfOriginal] == ' ':
              new_str[indexOfNew-2:indexOfNew+1] = ['%','2','0']
              indexOfNew -= 3
              indexOfOriginal -= 1
           else:
               new_str[indexOfNew] = s[indexOfOriginal]
               indexOfNew -= 1
               indexOfOriginal -= 1
        return ''.join(new_str)









if __name__ == '__main__':
    str1 = 'We Are Happy'
    s = Solution().replaceSpace(str1)
    print(s)