class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        n = len(nums)
        res = []

        for num in nums:
            heapq.heappush(res, num)

            if len(res) > k:
                heapq.heappop(res)

        return res[0]


