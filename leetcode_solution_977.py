class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left, right = 0, len(nums) - 1
        result = [0] * n
        index = n - 1
        while left <= right:
            if abs(nums[left]) < abs(nums[right]):
                result[index] = nums[right] ** 2
                right -= 1
            else:
                result[index] = nums[left] ** 2
                left += 1
            index -= 1
        return result