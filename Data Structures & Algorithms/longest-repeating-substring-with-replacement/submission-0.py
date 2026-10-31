class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hm={}
        maxlen=0
        maxfreq=0
        l=0
        for r in range(0,len(s)):
            hm[s[r]]=1+hm.get(s[r],0)
            maxfreq=max(maxfreq,hm[s[r]])
            while(((r-l+1))-maxfreq>k):
                hm[s[l]]-=1
                l+=1
            maxlen=max(maxlen,r-l+1)
        return maxlen