class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack, res = [], [0] * len(temperatures)

        for (i, temperature) in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < temperature:
                j = stack.pop()

                res[j] = i - j

            stack.append(i)

        return res