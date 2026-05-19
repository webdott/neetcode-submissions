class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operations = set(["+", "*", "/", "-"])

        for token in tokens:
            right = stack.pop() if token in operations else 0
            left = stack.pop() if token in operations else 0

            if token == "+":
                num = left + right
            elif token == "*":
                num = left * right
            elif token == "/":
                num = int(left / right)
            elif token == "-":
                num = left - right
            else:
                num = int(token)

            stack.append(num)

        return stack.pop()
