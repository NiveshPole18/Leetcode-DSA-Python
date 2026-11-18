class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        stack=[]
        greater={}

        for num in nums2:
            while stack and num > stack[-1]:
                prev=stack.pop()
                greater[prev]=num

            stack.append(num)

        result=[]

        for num in nums1:
            if num in greater:
                result.append(greater[num])

            else:
                result.append(-1)
        return result


