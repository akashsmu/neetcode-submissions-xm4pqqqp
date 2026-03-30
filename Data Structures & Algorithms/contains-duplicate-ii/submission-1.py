class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        numMap = {}
        for i, num in enumerate(nums):
            if num not in numMap:
                numMap[num] = i
                continue
            index = numMap[num]
            if abs(i - index) <= k:
                return True
            numMap[num] = i
        return False