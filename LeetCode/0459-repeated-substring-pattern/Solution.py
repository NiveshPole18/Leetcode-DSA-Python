class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        temp =s+s
        if s in temp[1:-1]:
            return True
        else:
            return False