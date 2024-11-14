from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        answer = [0] * n
        stk = [] 

        for i in range(n):
            while stk and temperatures[stk[-1]] < temperatures[i]:
                prev_index = stk.pop()
                answer[prev_index] = i - prev_index
            
            stk.append(i) 
        return answer
