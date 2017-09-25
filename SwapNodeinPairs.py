# coding=utf-8
# __author__ = 'xhm'
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        ans = head
        if not head:
            return ans
        if head.next:
            sec = head.next
            head.next = sec.next
            sec.next = head
            ans = sec
        else:
            return ans

        while head.next:
            if head.next.next:
                first = head.next
                second = head.next.next
                head.next = second
                first.next = second.next
                second.next = first
                head = first
            else:
                break

        return ans
