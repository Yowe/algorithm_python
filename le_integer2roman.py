#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = "Yowe"

'''
Given an integer, convert it to a roman numeral.

Input is guaranteed to be within the range from 1 to 3999.
'''

class Solution:
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num < 1 or num > 3999:
            raise Exception('num to be within the range from 1 to 3999')

