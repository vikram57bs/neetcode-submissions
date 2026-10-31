class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit=0
        n=len(prices)
        i=0
        while(i<n-1):
            j=i+1
            if(prices[i]<=prices[j]):
                while(j<n and prices[i]<=prices[j]):
                    profit=max(profit,prices[j]-prices[i])
                    j+=1
                i=j
            else:
                i+=1
        return profit