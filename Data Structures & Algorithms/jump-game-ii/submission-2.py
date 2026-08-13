class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        run_sum = 0
        steps = 0

        if n == 1:
            return steps

        for i in range(n):
            if i + nums[i] + 1 > n - 1:
                steps += 1
                return steps

            if run_sum == 0:
                run_sum = nums[i]
                steps += 1
            
            run_sum -= 1

        return steps