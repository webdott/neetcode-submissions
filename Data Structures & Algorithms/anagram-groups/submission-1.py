class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = dict()

        for word in strs:
            key = [0 for _ in range(26)]
            
            for char in word:
                key[ord(char) - ord('a')] += 1

            key = "".join(str(key))

            if key not in groups:
                groups[key] = []

            groups[key].append(word)

        return list(groups.values())