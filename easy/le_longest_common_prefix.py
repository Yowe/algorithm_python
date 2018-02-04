#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = "Yowe"

'''
查找字符串数组中最长的公共前缀字符串
'''


class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ""

        l = 1
        result = strs[0]
        while l < len(strs):
            result = self.commonPrefix(result, strs[l])
            l += 1
        return result

    # 拿第一个字符串和后面的比较，获得最长公共子串，然后拿子串和下一个对比
    def commonPrefix(self, origin, target):
        result = ''
        loop = len(target) if len(origin) > len(target) else len(origin)
        for i in range(0, loop):
            if target[i] == origin[i]:
                result += origin[i]
            else:
                break
        return result

so = Solution()
strs = ['a']
print(so.longestCommonPrefix(strs))