#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = "Yowe"

'''
判断一个数字是否是回文数
'''

class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False

        reverse = 0
        temp = x
        while x > 0:
            reverse = reverse*10 + x % 10
            x = int(x / 10)

        return reverse == temp

solu = Solution()
print(solu.isPalindrome(121))