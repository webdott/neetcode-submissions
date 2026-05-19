class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        pivot, l, r = 0, 0, n - 1

        while l < r:
            mid = (l + r) // 2

            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid
            
        pivot = l

        def bs(ns: List[int], target: int) -> int:
            n = len(ns)
            left, right = 0, n - 1

            print(left, right)

            while left <= right:
                mid = (left + right) // 2

                if ns[mid] == target:
                    return mid
                elif ns[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1

            return -1

        left = bs(nums[0:pivot], target)

        if left > -1:
            return left

        right = bs(nums[pivot:], target)
        return pivot + right if right > -1 else right