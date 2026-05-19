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
        res = [[]]

        def dfs(curr: [int], idx: int):
            if idx >= len(nums):
                res.append(curr[:])
                return

            for i in range(idx, len(nums)):
                curr.append(nums[idx])
                dfs(curr, i + 1)
                curr.pop()

        for i in range(len(nums)):
            dfs([], i)
            
        return res