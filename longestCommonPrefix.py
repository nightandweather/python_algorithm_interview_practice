class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        strs.sort(key=len)
        short = strs[0]
        for i, c in enumerate(short):
            for str in strs[1:]:
                if str[i] != c:
                    return short[:i]
        return short
