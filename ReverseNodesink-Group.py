# coding=utf-8
# __author__ = 'xhm'


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if k == 1:
            return head
        pre = self
        pre.next = head
        while pre.next:
            judge = pre.next
            for i in range(k-1):
                if judge.next:
                    judge = judge.next
                else:
                    return self.next
            last = pre.next
            now = pre.next.next
            for i in range(k-1):
                last.next = now.next
                now.next = pre.next
                pre.next = now
                now = last.next
            pre = last
        return self.next