class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        _hash = set(nums)
        res = 0
        seen = {}

        for num in nums:
            if num in seen:
                continue

            count = 0
            curr = num

            while curr in _hash:
                if curr in seen:
                    count += seen[curr]
                    break

                count += 1
                seen[curr] = 0
                curr += 1
            
            seen[num] = count
            res = max(res, count)

        return res
            