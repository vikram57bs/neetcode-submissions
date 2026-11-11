class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result=[]
        current=[]
        def dfs(index,remaining):
            if remaining==0:
                result.append(current.copy())
                return
            for i in range(index,len(nums)):
                if nums[i]>remaining:
                    continue
                current.append(nums[i])
                dfs(i,remaining-nums[i])
                current.pop()
        dfs(0,target)
        return result