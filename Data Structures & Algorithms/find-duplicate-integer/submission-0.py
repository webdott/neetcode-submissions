class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        i = 0

        while i != nums[i]:
            j = nums[i]
            nums[i] = i
            i = j

        return i