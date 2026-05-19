class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)
        _freq = defaultdict(list)
        values = []

        for num in nums:
            freq[num] += 1

        for key, value in freq.items():
            _freq[value].append(key)

            if _freq[value][0] == key:
                values.append(value)

        values.sort(reverse=True)

        res = []

        for value in values:
            for num in _freq[value]:
                res.append(num)
                k -= 1

            if k == 0:
                return res

        return res
            


        


        