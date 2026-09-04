class Solution:
    def isPalindrome(self, s: str) -> bool:
        begin, end = 0, len(s) - 1
        while begin < end:
            while begin < end and not self.alphaNum(s[begin]):
                begin += 1
            while end > begin and not self.alphaNum(s[end]):
                end -= 1
            if s[begin].lower() != s[end].lower():
                return False
            begin += 1
            end -= 1
        return True
    def alphaNum(self, c: chr) -> bool:
        return (ord('A') <= ord(c) <= ord('Z') or 
                ord('a') <= ord(c) <= ord('z') or
                ord('0') <= ord(c) <= ord('9'))