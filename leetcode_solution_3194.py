class Solution:
    def minimumAverage(self, nums):
        averages = []
        while len(nums) > 1:

            max_value = max(nums)
            min_value = min(nums)

            nums.remove(max_value)
            nums.remove(min_value)
            
            avg = (max_value + min_value)/2
            averages.append(avg)
        return min(averages) if averages else 0