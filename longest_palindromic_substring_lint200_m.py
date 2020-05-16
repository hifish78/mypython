import sys
class Solution:
    # please refer to palindromic_substring_leet647_m.py 
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ''
        self.longest = -sys.maxsize - 1
        self.res = ''
        for i in range(len(s)):
            self.helper(s, i, i)
            self.helper(s, i, i + 1)
        return self.res

    def helper(self, s, i, j):
        while i >= 0 and j < len(s) and s[i] == s[j]:
            if j - i + 1 > self.longest:
                self.res = s[i:j+1]
                self.longest = j - i + 1
            i -= 1
            j += 1