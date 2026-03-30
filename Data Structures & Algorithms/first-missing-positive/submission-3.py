class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        minValue, maxValue = min(nums) , max(nums)
        for num in range(1, maxValue + 1):
            if num not in nums: return num

        return maxValue + 1 if maxValue > 0 else 1