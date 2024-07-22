class Solution:
    def smallerNumbersThanCurrent(self, nums):
        sorted_nums = sorted((num, i) for i, num in enumerate(nums))
        counts = {}
        for i, (num, original_index) in enumerate(sorted_nums):
            if num not in counts:
                counts[num] = i
        result = [counts[num] for num in nums]
        return result