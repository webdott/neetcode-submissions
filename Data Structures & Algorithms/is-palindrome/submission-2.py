class Solution:
    def isPalindrome(self, s: str) -> bool:
        word = ""

        for char in s:
            word += char.lower() if char.isalnum() else ""

        n = len(word)
        left, right = 0, n - 1

        while right >= left:
            if word[left] != word[right]:
                return False

            left += 1
            right -= 1

        return True

        