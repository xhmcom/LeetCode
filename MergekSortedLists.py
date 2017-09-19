# coding=utf-8
# __author__ = 'xhm'
# Definition for singly-linked list.


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


MAX = 1000000000


class MinHeap:
    def __init__(self, lists):
        self.list = lists
        i = (len(self.list) - 2) // 2
        while i >= 0:
            self.adjust_heap(i)
            i -= 1

    def insert_heap(self, loc):
        if loc == 0:
            return
        if self.list[loc] < self.list[(loc - 1) // 2]:
            self.list[loc], self.list[(loc - 1) // 2] = self.list[(loc - 1) // 2], self.list[loc]
            self.insert_heap((loc - 1) // 2)
        else:
            return

    def adjust_heap(self, loc):
        if loc * 2 + 1 > len(self.list) - 1:
            return
        if loc * 2 + 1 == len(self.list) - 1:
            if self.list[loc] <= self.list[loc * 2 + 1]:
                return
            else:
                self.list[loc], self.list[loc * 2 + 1] = self.list[loc * 2 + 1], self.list[loc]
                return
        if self.list[loc] < self.list[loc * 2 + 1] and self.list[loc] < self.list[loc * 2 + 2]:
            return
        change = loc * 2 + 1
        if self.list[loc * 2 + 1] > self.list[loc * 2 + 2]:
            change = loc * 2 + 2
        self.list[loc], self.list[change] = self.list[change], self.list[loc]
        self.adjust_heap(change)

    def insert(self, i_num):
        self.list.append(i_num)
        length = len(self.list)
        self.insert_heap(length - 1)

    def min(self):
        if not self.list:
            return False
        return self.list[0]

    def pop(self):
        if not self.list:
            return False
        self.list[0], self.list[len(self.list) - 1] = self.list[len(self.list) - 1], self.list[0]
        result = self.list.pop()
        self.adjust_heap(0)
        return result


class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if not lists:
            return []
        ans = ListNode(MAX)
        head = ans
        initial_list = []
        doing_list = []
        for i in range(len(lists)):
            if lists[i]:
                initial_list.append(lists[i].val)
                doing_list.append(lists[i].val)
            else:
                lists[i] = ListNode(MAX)
                initial_list.append(MAX)
                doing_list.append(MAX)
        heap = MinHeap(doing_list)
        while True:
            if heap.min() == MAX:
                break
            ans.next = ListNode(MAX)
            ans = ans.next
            ans.val = heap.pop()
            num = initial_list.index(ans.val)

            if lists[num].next:
                lists[num] = lists[num].next
                initial_list[num] = lists[num].val
            else:
                initial_list[num] = MAX
            heap.insert(initial_list[num])
        return head.next


def main():
    testlist = [9, 1, 8]
    heap = MinHeap(testlist)
    heap.insert(5)
    print(heap.pop())
    print(heap.pop())
    print(heap.pop())

if __name__ == '__main__':
    main()