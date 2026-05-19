import bisect

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m, n = len(nums1), len(nums2)
        t_n = m + n

        l, r = (t_n // 2) - 1 if t_n % 2 == 0 else (t_n // 2), t_n // 2
        min_arr, max_arr = nums1 if m <= n else nums2, nums2 if m <= n else nums1

        for number in min_arr:
            idx_to_insert = bisect.bisect_left(max_arr, number)

            max_arr.insert(idx_to_insert, number)

        return (max_arr[l] + max_arr[r]) / 2

