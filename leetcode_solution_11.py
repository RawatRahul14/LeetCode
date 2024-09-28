class Solution:
    def maxArea(self, height) -> int:
        max_water = 0
        i, j = 0, len(height) - 1
        while i < j:
            water_vol = (j - i) * min(height[i], height[j])
            if water_vol > max_water:
                max_water = water_vol
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return max_water