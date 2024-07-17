class Solution:
    def moveZeroes(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        last_non_zero = 0
        for curr in range(len(nums)):
            if nums[curr] != 0:
                nums[last_non_zero], nums[curr] = nums[curr], nums[last_non_zero]
                last_non_zero += 1