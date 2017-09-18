# coding=utf-8
# __author__ = 'xhm'
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        num = 0
        node = head
        while node.next:
            num += 1
            node = node.next
        move = num - n + 1

        if move == 0:
            head = head.next
            return head
        num = 0
        node = head
        while num < move - 1:
            num += 1
            node = node.next
        node.next = node.next.next
        return head