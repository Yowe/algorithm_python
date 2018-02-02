#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = "Yowe"

'''
Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
       self.val = x
       self.next = None


class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # 数字之和，当和大于10时，进一位
        sum = 0
        # 头结点
        head = ListNode(0)
        # 头结点副本
        p = head
        while l1 or l2:
            sum = int(sum/10)
            if l1:
                sum += l1.val
                l1 = l1.next
            if l2:
                sum += l2.val
                l2 = l2.next

            p.next = ListNode(sum % 10)
            p = p.next

        return head.next

    def test(self):
        l1 = ListNode(7)
        l1.next = ListNode(1)
        l1.next.next = ListNode(2)

        l2 = ListNode(3)
        l2.next = ListNode(4)
        l2.next.next = ListNode(5)

        head = self.addTwoNumbers(l1=l1, l2=l2)
        while(head):
            print(head.val)
            head = head.next


solu = Solution()
solu.test()
