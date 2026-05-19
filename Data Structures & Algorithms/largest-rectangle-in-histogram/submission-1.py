class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
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
