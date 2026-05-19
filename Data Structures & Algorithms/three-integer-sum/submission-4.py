class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        left, right = 0, n - 1
        res = []

        while right > left:
            if numbers[left] + numbers[right] == target:
                curr_res = [numbers[left], numbers[right]]

                if not res or (res and res[-1] != curr_res):
                    res.append(curr_res)

                left += 1
                right -= 1
            elif  numbers[left] + numbers[right] > target:
                right -= 1
            else:
                left += 1

        return res 

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        res = []

        for idx, num in enumerate(nums):
            if num > 0:
                break

            if idx == 0 or num != nums[idx - 1]:
                other_two = self.twoSum(nums[idx + 1:], 0 - num)
                
                for pair in other_two:
                    curr_res = [num] + pair

                    if not res or (res and curr_res != res[-1]):
                        res.append(curr_res)

        return res

# -2 0 1 1 2
    