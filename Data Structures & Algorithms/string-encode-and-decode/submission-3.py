class Solution:
    def encode(self, strs: List[str]) -> str:
        res = ""

        for idx, s in enumerate(strs):
            if s == "":
                res += "EMPTY_STRING"
            
            res += s
            if idx < len(strs) - 1:
                res += "SEPARATOR"

        return res

    def decode(self, s: str) -> List[str]:
        return [] if s == "" else ["" if word == "EMPTY_STRING" else word for word in s.split("SEPARATOR")]