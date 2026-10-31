class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        leftprod=1
        rightprod=1
        totprod=1
        lp=[0] * len(nums)
        fa=[0]*len(nums)
        for i in range(len(nums)):
            lp[i]=leftprod
            leftprod*=nums[i]
        for j in range(len(nums)-1,-1,-1):
            totprod=lp[j]*rightprod
            fa[j]=totprod
            rightprod*=nums[j]
        return fa