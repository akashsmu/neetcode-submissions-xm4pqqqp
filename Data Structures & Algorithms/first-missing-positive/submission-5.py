class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # nums = set(nums)
        # maxValue =  max(nums)
        # for num in range(1, maxValue + 1):
        #     if num not in nums: return num

        # return maxValue + 1 if maxValue > 0 else 1
        n = len(nums)

        for i in range(n):
            while 1 <= nums[i] <= n and nums[nums[i]-1] != nums[i]:
                correct_idx = nums[i] - 1
                nums[i], nums[correct_idx] = nums[correct_idx], nums[i]

        for i in range(n):
            if nums[i] != i + 1:
                return i + 1

        return n + 1