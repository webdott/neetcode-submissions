class Solution:
    def isPalindrome(self, s: str) -> bool:
        word = ""

        for char in s:
            word += char.lower() if (65 <= ord(char) <= 90 or 97 <= ord(char) <= 122 or 48 <= ord(char) <= 57) else ""

        n = len(word)
        left, right = 0, n - 1

        while right >= left:
            print(word[left], word[right])
            if word[left] != word[right]:
                return False

            left += 1
            right -= 1

        return True

        