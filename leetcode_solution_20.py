class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2 == 1:
            return False
        stack = []
        matching_brackets = {
            ")": "(",
            "}": "{",
            "]": "["
        }
        for char in s:
            # Closing Bracket
            if char in matching_brackets:
                if not stack or stack[-1] != matching_brackets[char]:
                    return False
                stack.pop()
            # Opening Bracket
            else:
                stack.append(char)
        return len(stack) == 0