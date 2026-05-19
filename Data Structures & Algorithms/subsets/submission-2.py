class Solution:
    def subsets1(self, nums: List[int]) -> List[List[int]]:
        res = [[]]

        for num in nums:
            l = len(res)
            for i in range(l):
                sub = res[i]
                p = sub[:]
                p.append(num)
                res.append(p)

        return res

    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(curr: [int], idx: int):
            if idx >= len(nums):
                res.append(curr[:])
                return

            curr.append(nums[idx])
            dfs(curr, idx + 1)
            curr.pop()
            dfs(curr, idx + 1)

        dfs([], 0)

        return res