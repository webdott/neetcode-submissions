class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix_prod = [1]
        suffix_prod = [1]
        ans = []

        for i in range(n):
            prefix_prod.append(prefix_prod[-1] * nums[i])
            suffix_prod.append(suffix_prod[-1] * nums[n - i - 1])

        m = len(suffix_prod)

        for i in range(n):
            ans.append(prefix_prod[i] * suffix_prod[m - i - 2])

        return ans