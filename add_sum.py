#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = "Yowe"

'''
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
'''


class solu:
    def two_sum(self, num, target):
        dict = {}
        for i in range(len(num)):
            x = num[i]
            if target - x in dict:
                return dict[target-x]+1, i+1
            dict[x] = i


so = solu()
nums = [2, 11, 15, 7]
print(so.two_sum(nums, 9))