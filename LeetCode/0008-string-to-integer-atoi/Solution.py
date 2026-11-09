class Solution:
    def myAtoi(self, s: str) -> int:
        i = 0
        num = 0
        sign = 1

        # Skip spaces
        while i < len(s) and s[i] == ' ':
            i += 1

        # Check sign
        if i < len(s) and s[i] == '-':
            sign = -1
            i += 1
        elif i < len(s) and s[i] == '+':
            i += 1

        # Convert digits
        while i < len(s) and s[i].isdigit():
            num = num * 10 + int(s[i])
            i += 1

        num = num * sign

        # Handle 32-bit integer limits
        num = max(-2**31, min(num, 2**31 - 1))

        return num