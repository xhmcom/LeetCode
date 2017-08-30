# coding=utf-8
# __author__ = 'xhm'


def find_b(arr, start, end, x):
    mid = (start + end) / 2
    if arr[mid] == x:
        return mid
    if arr[mid] > x:
        if mid - 1 < 0:
            return -1
        if arr[mid-1] < x:
            return mid-1
        return find_b(arr, start, mid, x)
    else:
        if mid + 1 >= len(arr):
            return len(arr)
        if arr[mid+1] > x:
            return mid
        return find_b(arr, mid+1, end, x)

def re_find_median(nums1, nums2, k, odd):
    m = len(nums1)
    n = len(nums2)
    a_median = nums1[m / 2]
    b_finded = find_b(nums2, 0, n, a_median)
    head_num = (m / 2 + 1) + b_finded
    if head_num == k:
        if odd == 0:
            return
        else:
            return nums1[m/2]


class Solution(object):


    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        m = len(nums1)
        n = len(nums2)
        k = (m+n)/2
        if (m+n)%2 == 0:
            odd = 0
        else:
            odd = 1
        re_find_median(nums1, nums2, k, odd)


a = {1, 3, 5, 7, 9}
b = {2, 4, 6, 8, 10}
input_test = Solution()
input_test.findMedianSortedArrays(a, b)
