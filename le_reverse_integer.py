#!/usr/bin/python
# -*- coding: utf-8 -*-

import  sys
__author__ = "Yowe"
import math

'''
Given a 32-bit signed integer, reverse digits of an integer.

Input: 123
Output:  321

Input: -123
Output: -321
'''

class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """

        print(int(str(x)[::2]))
        return 0

        result = 0
        if x > 2147483647:
            return result

        sign = 1 if x > 0 else -1
        x = abs(x)
        while x > 0:
            result = (result*10 + x % 10)
            x = int(x/10)

        print(result*sign)

solu = Solution()
solu.reverse(1534236469)