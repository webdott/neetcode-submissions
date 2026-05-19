class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash_set = defaultdict(int)

        for char in s:
            hash_set[char] += 1

        for char in t:
            if char not in hash_set:
                return False

            hash_set[char] -= 1

            if hash_set[char] == 0:
                del hash_set[char]

        return len(hash_set) == 0
