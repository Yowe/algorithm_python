#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = "Yowe"

'''
Given a non-negative integer represented as a non-empty array of digits, plus one to the integer.

You may assume the integer do not contain any leading zero, except the number 0 itself.

The digits are stored such that the most significant digit is at the head of the list.

'''


class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        d_len = len(digits)
        # 列表长度为0，直接返回列表
        if d_len == 0:
            return digits

        # 列表索引变化，如无变化说明最后一个数字小于9，直接返回
        index = -1

        for i in range(0, d_len):
            if digits[d_len-i-1] < 9:
                digits[d_len-i-1] = (digits[d_len-i-1]+1)
                return digits
            else:
                index = i
                digits[d_len-i-1] = 0

        # 走到这一步，说明列表所有数字都进位，则增加列表长度
        new_nums = []
        for i in range(0, d_len+1):
            if i == 0:
                new_nums.append(1)
            else:
                new_nums.append(0)
        return new_nums

nums = [1,7,9]
solu = Solution()
print(solu.plusOne(nums))