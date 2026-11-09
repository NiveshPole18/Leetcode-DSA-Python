class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        for ch in s:
            if ch=="(" or ch=="{" or ch=="[":
                stack.append(ch)
            else:
                if not stack:
                    return False

                last=stack.pop()

                if ch==")"and last!="(":
                    return False
                if ch=="}"and last!="{":
                    return False
                if ch=="]"and last!="[":
                    return False
        return len(stack)==0