class Solution:
    def trap(self, height: List[int]) -> int:
        # if bar is 0, skip
        # if not 0, find a bar as high or higher, 
            # or when we get to the last non-zero bar
        # then find the lower of the two:
        # all bars in between, add difference between min bar and that bar

        # E.g
        # Res = 0
        # 2 -> Next tall or taller bar: 3
            # Min between the two: 2
            # Bars in between: 
                # 0 -> Difference = 2
                # Res += 2 = 2

        # 3 -> Next tall or taller bar: 3
            # Min between the two: 3
            # Bars in between: 
                # 1 -> Difference = 2
                # 0 -> Difference = 3
                # 1 -> Difference = 2
                # Res += 7 = 9
            
        # 3 -> Next tall or taller bar: 1
            # Min between the two: 1
            # Bars in between: 
                # 2 -> Difference = -1 (0)
                # 1 -> Difference = 0
                # Res += 0 = 9

        left, right, res, n = 0, 1, 0, len(height)

        if n < 3:
            return 0

        while left < n > right:
            while right < n - 1 and height[right] < height[left]:
                right += 1

            _min, curr = min(height[left], height[right]), 0

            for i in range(left + 1, right):
                curr += max(0, _min - height[i])

            res += curr

            if height[right] >= height[left] or curr > 0:
                left = right
            else:
                left += 1

            right = left + 1

        return res



