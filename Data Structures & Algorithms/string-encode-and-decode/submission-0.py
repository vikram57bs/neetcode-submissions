class Solution:
    def encode(self, strs: List[str]) -> str:
        result=""
        for i in strs:
            result+=str(len(i))+"#"+i
        return result
    def decode(self, s: str) -> List[str]:
        i=0
        ll=[]
        while i<len(s):
            j=i
            while s[j]!="#":
                j+=1
            leng=int(s[i:j])
            word=s[j+1:j+1+leng]
            ll.append(word)
            i= j+1+leng
        return ll
