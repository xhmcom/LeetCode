# coding=utf-8
# __author__ = 'xhm'
class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        closest = 1000000000
        nums.sort()
        first = 0
        result = 0
        while first < len(nums) - 2:
            i = first + 1
            j = len(nums) - 1
            while i < j:
                ans = nums[first] + nums[i] + nums[j]
                if closest > abs(ans - target):
                    closest = abs(ans - target)
                    result = ans
                if ans < target:
                    i += 1
                    while nums[i] == nums[i - 1] and i < j:
                        i += 1
                if ans > target:
                    j -= 1
                    while nums[j] == nums[j + 1] and i < j:
                        j -= 1
                if ans == target:
                    return result
            first += 1
            while nums[first] == nums[first - 1] and first < len(nums) - 2:
                first += 1
        return result
