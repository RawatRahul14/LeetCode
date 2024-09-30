class Solution:
    def containsDuplicate(self, nums) -> bool:
        s = len(set(nums))
        o = len(nums)
        if s == o:
            return False
        return True