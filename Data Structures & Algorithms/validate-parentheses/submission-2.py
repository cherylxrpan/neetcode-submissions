class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        paired = {')': '(', ']': '[', '}': '{'} 
        for char in s:
            if char in paired:
                if stack and stack[-1] == paired[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)

        return True if not stack else False
