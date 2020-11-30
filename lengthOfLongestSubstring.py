from collections import defaultdict

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ma = i = j = 0
        d = defaultdict(lambda: -1)
        while j < len(s):
            if d[s[j]] >= i:
                i = d[s[j]] + 1
            if j - i + 1 > ma:
                ma = j - i + 1
            d[s[j]] = j
            j += 1
            
        return ma
