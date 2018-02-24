#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = "Yowe"

'''
查找字符串中最长的子字符串的长度，子字符串不包含重复字符
Given "abcabcbb", the answer is "abc", which the length is 3.
'''


class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic = {}
        res = 0
        start = 0
        for i, ch in enumerate(s):
            if ch in dic:
                res = max(res, i-start)
                start = max(start, dic[ch]+1)
            dic[ch] = i

        return max(res, len(s) - start)

so = Solution()
str = 'abcabcd'
print(so.lengthOfLongestSubstring(str))






