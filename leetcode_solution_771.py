class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        count = 0
        dic = {}
        for stone in stones:
            if stone in dic:
                dic[stone] += 1
            else:
                dic[stone] = 1
        for jewel in jewels:
            if jewel in dic:
                count += dic[jewel]
        return count