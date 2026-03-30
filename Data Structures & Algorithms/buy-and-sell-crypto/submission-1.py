class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # res = 0
        # for i in range(len(prices)):
        #     for j in range(i+1,len(prices)):
        #         res = max(res, prices[j]-prices[i])
        # return res
        res = 0
        minValue = prices[0]
        for i in range(1,len(prices)):
            if prices[i] < minValue:
                minValue = prices[i]
                continue
            res = max(res, prices[i] - minValue)
        return res