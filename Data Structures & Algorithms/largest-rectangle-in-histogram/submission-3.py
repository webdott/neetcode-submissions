class Solution:
    def largestRectangleAreaNaive(self, heights: List[int]) -> int:
        n = len(heights)
        res = 0

        for i in range(n):
            min_height = heights[i]
            res = max(res, heights[i]) 
            j = i

            while j >= 0:
                min_height = min(min_height, heights[j])
                res = max(res, min_height * (i - j + 1)) 
                j -= 1

        return res

    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        res = 0
        stack = []

        for i, h in enumerate(heights):
            start = i

            while stack and stack[-1][1] >= h:
                index, height = stack.pop()

                res = max(res, height * (i - index))
                start = index

            stack.append((start, h))

        for i, h in stack:
            res = max(res, h * (n - i))

        return res
