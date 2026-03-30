class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxWater = float("-inf")
        l,r=0,len(heights) -1
        while l<r:
            amount = min(heights[l], heights[r]) * (r-l)
            maxWater = max(maxWater, amount)
            if heights[l] < heights[r]:
                l+=1
            else:
                r-=1
        return maxWater

        