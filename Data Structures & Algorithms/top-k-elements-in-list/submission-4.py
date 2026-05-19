class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)
        bucket = [[] for _ in range(len(nums) + 1)]

        for num in nums:
            freq[num] += 1

        for key, value in freq.items():
            bucket[value].append(key)

        res = []

        for i in range(len(bucket) - 1, 0, -1):
            if k <= 0:
                return res

            b = bucket[i]

            res += b[:k]
            k -= len(b)

        return res
        


        