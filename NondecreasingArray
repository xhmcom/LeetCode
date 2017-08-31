def if_decreasing(nums, times):
    for i in range(1, len(nums)):
        if nums[i-1] > nums[i]:
            if times == 0:
                remove_1 = nums[:]
                del (remove_1[i - 1])
                remove_2 = nums[:]
                del (remove_2[i])
                if if_decreasing(remove_1, 1) or if_decreasing(remove_2, 1):
                    return 1
                else:
                    return 0
            else:
                return 0
    return 1


class Solution(object):
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        decreasing = if_decreasing(nums, 0)
        if decreasing:
            return True
        return False
