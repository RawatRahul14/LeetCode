class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """

        i, e = 0, len(s)-1
        while i < e:
            s[i], s[e] = s[e], s[i]
            i, e = i + 1, e - 1
        