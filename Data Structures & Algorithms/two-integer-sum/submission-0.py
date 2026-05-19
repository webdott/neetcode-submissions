class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_set = dict()

        for idx, num in enumerate(nums):
            if num in hash_set:
                return [hash_set[num], idx]

            key = target - num
            
            if key in hash_set:
                continue

            hash_set[key] = idx

        return []