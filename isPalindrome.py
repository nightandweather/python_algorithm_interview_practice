class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        revrse = int(str(x)[::-1])
        return True if revrse == x else False
