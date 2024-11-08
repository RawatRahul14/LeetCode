class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack_score = []
        for i in operations:
            if i == "+":
                stack_score.append(stack_score[-1] + stack_score[-2])
            elif i == "D":
                stack_score.append(stack_score[-1] * 2)
            elif i == "C":
                stack_score.pop()
            else:
                stack_score.append(int(i))
        return sum(stack_score)