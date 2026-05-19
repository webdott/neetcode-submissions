class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]

        for num in nums:
            l = len(res)
            for i in range(l):
                sub = res[i]
                p = sub[:]
                p.append(num)
                res.append(p)

        return res