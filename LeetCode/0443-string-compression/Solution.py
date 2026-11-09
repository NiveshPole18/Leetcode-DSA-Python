class Solution:
    def compress(self, chars: List[str]) -> int:
        i = 0
        ans = 0

        while i < len(chars):
            ch = chars[i]
            count = 0

            while i < len(chars) and chars[i] == ch:
                count += 1
                i += 1

            chars[ans] = ch
            ans += 1

            if count > 1:
                for digit in str(count):
                    chars[ans] = digit
                    ans += 1

        return ans