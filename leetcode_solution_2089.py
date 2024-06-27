class Solution:
    def targetIndices(self, nums, target):
        nums.sort()
        indices = []
        for i in range(len(nums)):
            if nums[i] - target == 0:
                indices.append(i)
        return indices