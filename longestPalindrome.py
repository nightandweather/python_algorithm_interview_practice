class Solution:
    def longestPalindrome(self, s: str) -> str:
        

        if len(s) <= 1:
            return s

        start, end, i = 0, 1, 0

        while i < len(s):
            if len(s) - i <= end / 2:
                break

            j, k = i, i

            while k < len(s) - 1 and s[k] == s[k + 1]:
                k += 1

            i = k + 1
            while k < len(s) - 1 and j and s[k + 1] == s[j - 1]:
                k = k + 1
                j = j - 1

            if k - j + 1 > end:
                start = j
                end = k - j + 1

           
        return s[start: start + end]

