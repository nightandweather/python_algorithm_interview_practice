class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman_to_int = {"I": 1, "V": 5, "X": 10, "L": 50, "C":100, "D": 500, "M": 1000}
        num_int = 0

        for roman_char in range(0, len(s)):
            if roman_char < len(s) - 1 and roman_to_int[s[roman_char]] < roman_to_int[s[roman_char + 1]]:
                num_int = num_int - roman_to_int[s[roman_char]]
            else:
                num_int = num_int + roman_to_int[s[roman_char]]
                
        return num_int
