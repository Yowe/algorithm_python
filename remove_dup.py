#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = "Yowe"

'''
Given a sorted array, remove the duplicates in-place such that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
'''

class Solution:
    def removeDuplicates(self, nums):
        """
        :type num: int
        :rtype: str
        """
        if len(nums) == 0:
            return 0

        i = 0
        for j, n in enumerate(nums):
            if j > 0:
                if nums[j] != nums[i]:
                    nums[i+1] = nums[j]
                    i += 1
        print(nums)
        return i+1


solu = Solution()
nums = [1, 1, 2]
print(solu.removeDuplicates(nums))
