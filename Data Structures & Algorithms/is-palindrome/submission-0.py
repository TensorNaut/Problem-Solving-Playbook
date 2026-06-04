import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.strip()
        s = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        n = len(s)
        for i in range(n//2):
            if s[i] != s[-(i+1)]:
                return False
        return True