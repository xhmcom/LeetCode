# coding=utf-8
# __author__ = 'xhm'


class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        bj = 0
        for i in range(len(nums) - 1, 0, -1):
            if nums[i] > nums[i - 1]:
                for j in range(i, len(nums)):
                    if nums[j] <= nums[i - 1]:
                        nums[j - 1], nums[i - 1] = nums[i - 1], nums[j - 1]
                        nums[i:len(nums)] = sorted(nums[i:len(nums)])
                        bj = 1
                        break
                if not bj:
                    nums[len(nums) - 1], nums[i - 1] = nums[i - 1], nums[len(nums) - 1]
                    nums[i:len(nums)] = sorted(nums[i:len(nums)])

                    bj = 1
                break

        if not bj:
            nums.sort()
