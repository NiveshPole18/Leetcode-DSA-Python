class Solution:
    def isCovered(self, ranges, left, right):

        for num in range(left, right + 1):

            covered = False

            for start, end in ranges:

                if start <= num and num <= end:
                    covered = True
                    break

            if not covered:
                return False

        return True