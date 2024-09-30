from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashmap = Counter(s)
        if len(s) != len(t):
            return False
        for w in t:
            if hashmap[w] > 0:
                hashmap[w] -= 1
            else:
                return False
        return True 