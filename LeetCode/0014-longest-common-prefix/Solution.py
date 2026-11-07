class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        prefix=strs[0]

        for word in strs:
            while word[:len(prefix)]!=prefix:
                prefix=prefix[:-1]

        return prefix