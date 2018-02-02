#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = "Yowe"

'''
Implement strStr().

Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
'''


class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        index = -1

        if len(haystack) == 0 and len(needle) == 0:
            index = 0

        ne_len = len(needle)
        for i in range(len(haystack)):
            to_index = i+ne_len
            if haystack[i:to_index] == needle:
                index = i
                break

        return index


solu = Solution()
haystack = "hello"
needle = "ll"
solu.strStr(haystack, needle)