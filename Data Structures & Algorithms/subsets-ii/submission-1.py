class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        self.ans = []
        nums.sort()

        self.bt(nums, [], 0)
        
        return self.ans

    def bt(self, nums:List[int], subset: List[int], idx: int):
        n = len(nums)

        if idx == n:
            self.ans.append(subset[:])
            return

        j = idx
        while j < n - 1 and nums[j] == nums[j + 1]:
            j += 1

        self.bt(nums, subset, j + 1)
        subset.append(nums[idx])
        self.bt(nums, subset, idx + 1)
        subset.pop()
            
