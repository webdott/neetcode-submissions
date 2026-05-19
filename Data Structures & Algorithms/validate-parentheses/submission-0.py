class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        stack_map = {"]":"[", ")":"(", "}":"{"}

        for char in s:
            if char == "]" or char == "}" or char == ")":
                if stack and stack[-1] == stack_map[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)

        return not stack