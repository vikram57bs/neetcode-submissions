from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq=Counter(nums)
        n=len(nums)
        bucket=[[] for i in range(n+1)]
        ans=[]
        for nn,c in freq.items():
            bucket[c].append(nn)
        for i in range(n,0,-1):
            for num in bucket[i]:
                ans.append(num)
                if len(ans)==k:
                    return ans