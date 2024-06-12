class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        sum_miss = (n * (n+1)) // 2
        return sum_miss - sum(nums)