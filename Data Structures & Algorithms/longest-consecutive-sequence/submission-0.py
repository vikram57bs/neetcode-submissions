class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hs=set(nums)
        longest=0
        for n in hs:
            if n-1 not in hs:
                curr=n
                long=1
                while curr+1 in hs:
                    curr+=1
                    long+=1
                longest=max(long,longest)
        return longest