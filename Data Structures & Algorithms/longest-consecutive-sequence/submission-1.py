class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # store all numbers in a map

        # for each number, start counting 1 up until we get to where 1 isn't greater. Store result.

        # If we see a number less, start counting until we see a seen value

        # store highest

        map_set = set()
        seen = defaultdict(int)

        for num in nums:
            map_set.add(num)

        longest = 0

        for num in nums:
            if num in seen:
                continue

            curr_num = num
            count = 1

            while curr_num + 1 in map_set:
                if curr_num + 1 in seen:
                    count += seen[curr_num + 1]
                    break

                seen[curr_num + 1] = 0
                count += 1
                curr_num += 1

            seen[num] = count
            longest = max(longest, count)

        return longest


