class Solution(object):
    def isPalindrome(self, x):
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        original_x = x
        reversed_half = 0

        while x > reversed_half:
            last_digit = x % 10
            reversed_half = reversed_half * 10 + last_digit
            x //= 10

        return x == reversed_half or x == reversed_half // 10
