class Solution:
    def alphanum(self, c):
        return c.isalnum()

    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1

        while left < right:
            if not self.alphanum(s[left]):
                left += 1
                continue

            if not self.alphanum(s[right]):
                right -= 1
                continue

            if s[left].lower() != s[right].lower():
                return False

            left += 1
            right -= 1

        return True
