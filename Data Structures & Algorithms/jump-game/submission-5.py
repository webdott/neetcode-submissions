class Solution:
    def canJumpDP(self, nums: List[int]) -> bool:
        memo = [None] * len(nums)

        def dfs(i) -> bool:
            if i >= len(nums) - 1:
                return True

            if nums[i] == 0:
                return False

            if memo[i]:
                return memo[i]
            
            ans = False

            for j in range(1, nums[i] + 1):
                ans |= dfs(i + j)

            memo[i] = ans
            return memo[i]

        return dfs(0)

    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [False] * n

        dp[n - 1] = True

        for i in range(n - 2, -1, -1):
            for j in range(i + 1, i + nums[i] + 1):
                dp[i] = dp[i] or dp[j]

        return dp[0]