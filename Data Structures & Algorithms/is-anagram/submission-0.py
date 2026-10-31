class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hm1={}
        hm2={}
        for i in s:
            if i in hm1:
                hm1[i]+=1
            else:
                hm1[i]=1
        for i in t:
            if i in hm2:
                hm2[i]+=1
            else:
                hm2[i]=1
        if hm1==hm2:
            return True
        else:
            return False
        