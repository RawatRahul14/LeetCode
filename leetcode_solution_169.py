class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashtable = Counter(nums)
        for k, v in hashtable.items():
            if v > len(nums)//2:
                return k