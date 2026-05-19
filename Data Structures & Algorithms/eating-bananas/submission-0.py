class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        res = float('inf')

        while left <= right:
            mid = (left + right) // 2
            h_ = h

            for pile in piles:
                if h_ <= 0:
                    h_ = -1
                    break

                h_ -= math.ceil(pile / mid)

            if h_ >= 0:
                res = min(res, mid)
                right = mid - 1
            else:
                left = mid + 1

        return res