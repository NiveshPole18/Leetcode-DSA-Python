class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        n=len(nums)

        total=n*(n+1)//2
        for i in nums:
            total-=i

        return total