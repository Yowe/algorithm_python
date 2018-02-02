#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = "Yowe"

'''
合并两个已排序的链表，并将其作为一个新列表返回。
新的列表应该通过拼接前两个列表的节点来完成。
'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = ListNode(0)
        cur = head
        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next

        cur.next = l1 or l2
        return head.next


    def test(self):
        l1 = ListNode(5)
        l2 = ListNode(1)
        l2.next = ListNode(3)
        l2.next.next = ListNode(4)

        result = self.mergeTwoLists(l1, l2)
        while result:
            print(result.val)
            result = result.next

solu = Solution()
solu.test()



