class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue = []

        l, res = 0, []

        for r in range(len(nums)):
            queue.append(nums[r])

            if r - l + 1>= k:
                res.append(heapq.nlargest(1, queue[max(0, r - k + 1):])[0])

        return res