class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        n = len(nums)

        def dfs(curr: List[int], curr_sum: int, i: int):
            if curr_sum == target:
                res.append(curr[:])
                return

            if i >= n:
                return

            r_sum = curr_sum
            r_curr = curr[:]

            while r_sum + nums[i] <= target:
                r_sum += nums[i]
                r_curr.append(nums[i])
                dfs(r_curr, r_sum, i + 1)

            dfs(curr, curr_sum, i + 1)

        dfs([], 0, 0)

        return res