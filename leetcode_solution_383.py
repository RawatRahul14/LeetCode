from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        hashmap = Counter(magazine)
        for w in ransomNote:
            if hashmap[w] > 0:
                hashmap[w] -= 1
            else:
                return False
        return True