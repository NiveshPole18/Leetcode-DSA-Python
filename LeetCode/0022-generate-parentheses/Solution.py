class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        result=[]

        def backtracks(s,left,right):
            if len(s)==2*n:
                result.append(s)
                return 

            if left<n:
                backtracks(s+ "(",left+1,right)

            if right < left:
                backtracks(s+ ")",left,right+1)

        backtracks("",0,0)
        return result
