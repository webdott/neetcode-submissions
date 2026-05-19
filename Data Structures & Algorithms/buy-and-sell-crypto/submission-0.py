class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res, n = 0, len(prices)

        left, right = 0, 0
        
        while right < n:
            if prices[right] <= prices[left]:
                left = right
            else:
                res = max(res, prices[right] - prices[left])

            right += 1

        return res