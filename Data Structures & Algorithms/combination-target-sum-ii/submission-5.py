class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res, n = [], len(candidates)

        candidates.sort()

        def dfs(curr: List[int], i: int, curr_sum: int):
            if curr_sum == target:
                res.append(curr[:])
                return

            if i >= n or curr_sum > target:
                return


            curr.append(candidates[i])
            dfs(curr, i + 1, curr_sum + candidates[i])
            curr.pop()

            while i + 1 < n and candidates[i] == candidates[i + 1]:
                i += 1

            dfs(curr, i + 1, curr_sum)

        dfs([], 0, 0)

        return res
