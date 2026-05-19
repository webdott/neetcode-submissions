class Solution:
    def findMin(self, nums: List[int]) -> int:
        if nums[0] < nums[-1]:
            return nums[0]

        n = len(nums)
        left, right = 0, n - 1

        while left <= right:
            mid = (left + right) // 2

            if mid - 1 >= 0 and nums[mid] < nums[mid - 1]:
                return nums[mid] 
            elif nums[mid] < nums[0]:
                right = mid - 1
            else:
                left = mid + 1
 
        return nums[0]