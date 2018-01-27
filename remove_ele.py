#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = "Yowe"

'''
Given an array and a value, remove all instances of that value in-place and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

The order of elements can be changed. It doesn't matter what you leave beyond the new length.
'''


class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        i = 0
        for j, num in enumerate(nums):
            if num != val:
                nums[i] = nums[j]
                i += 1

        print(nums)
        return i


solu = Solution()
nums = [3, 3, 2, 2]
print(solu.removeElement(nums, 3))
