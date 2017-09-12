# coding=utf-8
# __author__ = 'xhm'
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        nums.sort()
        first = 0
        while first < len(nums)-2:
            if nums[first] > 0:
                break
            i = first + 1
            j = len(nums) - 1
            while i < j:
                ans = nums[first] + nums[i] + nums[j]
                if ans == 0:
                    result.append([nums[first], nums[i], nums[j]])
                if ans >= 0:
                    j -= 1
                    while nums[j] == nums[j+1] and i < j:
                        j -= 1
                if ans <= 0:
                    i += 1
                    while nums[i] == nums[i-1] and i < j:
                        i += 1
            first += 1
            while nums[first] == nums[first - 1] and first < len(nums) - 2:
                first += 1
        return result

