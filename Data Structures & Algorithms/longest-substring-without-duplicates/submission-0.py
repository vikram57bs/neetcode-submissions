class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ll=set()
        maxlen=0
        i=j=0
        n=len(s)
        while(j<n and i<n):
            if(s[j] not in ll):
                ll.add(s[j])
            else:
                while(s[j] in ll):
                    if(len(ll)>0):
                        ll.remove(s[i])
                        i+=1
                    else:
                        i=j
                ll.add(s[j])
            maxlen=max(maxlen,j-i+1)
            j+=1
        return maxlen