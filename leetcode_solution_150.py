from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack_tokens = []
        
        for i in tokens:
            if i == "+":
                b = stack_tokens.pop()
                a = stack_tokens.pop()
                stack_tokens.append(a + b)
            elif i == "-":
                b = stack_tokens.pop()
                a = stack_tokens.pop()
                stack_tokens.append(a - b)
            elif i == "*":
                b = stack_tokens.pop()
                a = stack_tokens.pop()
                stack_tokens.append(a * b)
            elif i == "/":
                b = stack_tokens.pop()
                a = stack_tokens.pop()
                stack_tokens.append(int(a / b))
            else:
                stack_tokens.append(int(i))
        
        return stack_tokens[0]