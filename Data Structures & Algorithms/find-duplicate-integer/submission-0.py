class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        count = Counter(nums)
        for num in range(len(nums)+1):
            if count[num] > 1:
                return num
                