class Solution:
    def dailyTemperaturesStack(self, temperatures: List[int]) -> List[int]:
        stack, res = [], [0] * len(temperatures)

        for (i, temperature) in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < temperature:
                j = stack.pop()

                res[j] = i - j

            stack.append(i)

        return res
    
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [0] * n

        for i in range(n - 2, -1, -1):
            j = i + 1

            while j < n and temperatures[j] <= temperatures[i]:
                if res[j] == 0:
                    j = n
                    break
                
                j += res[j]

            if j < n:
                res[i] = j - i

        return res