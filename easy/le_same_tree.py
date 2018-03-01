#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = "Yowe"

'''
在数组中找到相邻的子数组(包含至少一个数字)，它的和是最大的。

Given two binary trees, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical and the nodes have the same value.
'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
       self.val = x
       self.left = None
       self.right = None

class Solution:
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if not q and not p:
            return True
        elif not p or not q:
            return False
        elif p.val!=q.val:
            return False
        else:
            return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)