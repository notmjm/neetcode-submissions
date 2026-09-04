class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        begin = 0
        end = len(s) - 1
        while begin != end and begin < len(s) and end > -1:
            if s[begin].isalnum() and s[end].isalnum():
                if s[begin] != s[end]:
                    return False
                else:
                    begin += 1
                    end -= 1
            elif not s[begin].isalnum():
                begin += 1
            elif not s[end].isalnum():
                end -= 1
        return True