class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left, right = 0, len(s) - 1
        for _ in range(len(s) // 2):
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1