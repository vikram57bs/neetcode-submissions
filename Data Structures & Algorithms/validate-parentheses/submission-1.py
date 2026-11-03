class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        pairs={'(':')','{':'}','[':']'}
        for i in s:
            if i in ['(','{','[']:
                stack.append(i)
            else:
                if(stack and pairs[stack[-1]]==i):
                    stack.pop()
                else:
                    return False
        if(len(stack)>0):
            return False
        else:
            return True