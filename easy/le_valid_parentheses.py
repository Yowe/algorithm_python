#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = "Yowe"

'''
给定一个字符串，只包含字符('，')，“{”，“}”，'['和']'，确定输入字符串是否有效。
括号必须以正确的顺序关闭。”和“()(){ }”都是有效的
但是“(]”和“([)]是无效的。
'''
class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        stack = []
        dict = {"]": "[", "}": "{", ")": "("}
        for char in s:
            if char in dict.values():
                stack.append(char)
            elif char in dict.keys():
                if stack == [] or dict[char] != stack.pop():
                    return False
            else:
                return False
        return stack == []

so = Solution()
str = '([)]'
print(so.isValid(str))


