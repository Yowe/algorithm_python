#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = "Yowe"

'''
给定一个排序数组和一个目标值，如果找到目标，返回索引。如果没有，则返回按顺序插入的索引。
您可以假定数组中没有副本。
Input: [1,3,5,6], 5
Output: 2

Input: [1,3,5,6], 2
Output: 1

Input: [1,3,5,6], 2
Output: 1
'''

class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if target < nums[0]:
            return 0
        if target > nums[-1]:
            return len(nums)

        for i, num in enumerate(nums):
            if num == target:
                return i
            if num < target < nums[i+1]:
                return i+1

    def searchInsert2(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        low = 0
        high = len(nums)-1

        while low <= high:
            mid = int((low + high)/2)
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1

        return low



nums = [1, 3, 5 ,7]
solu = Solution()
print(solu.searchInsert2(nums,6))



