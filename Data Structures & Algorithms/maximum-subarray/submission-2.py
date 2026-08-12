class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        run_sum = -10001
        ans = -1

        for num in nums:
            ans = max(run_sum, ans)

            if num + run_sum < num:
                run_sum = num
                continue

            run_sum += num

        ans = max(run_sum, ans)

        return ans
