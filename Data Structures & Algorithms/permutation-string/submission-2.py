class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        set1 = {}

        for char in s1:
            set1[char] = 1 + set1.get(char, 0)

        l = 0

        set2 = {}

        for r in range(len(s2)):
            set2[s2[r]] = 1 + set2.get(s2[r], 0)

            while set2[s2[l]] > set1.get(s2[l], 0) and l < r:
                set2[s2[l]] -= 1
                l += 1 

            if set2[s2[r]] > set1.get(s2[r], 0):
                while l < r:
                    set2[s2[l]] -= 1
                    l += 1
                continue


            if r - l + 1 == len(s1):
                return True

        return False

# {k: 1, y: 1}
# 0, 0, {l: 0, e: 0, c: 1, a: 2}