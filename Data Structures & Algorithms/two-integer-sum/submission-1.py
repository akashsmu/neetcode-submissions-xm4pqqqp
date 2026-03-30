class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indexMap ={}
        for i, n in enumerate(nums):
            indexMap[n] = i

        for i in range(len(nums)):
            remainder = target - nums[i]
            if remainder in indexMap and indexMap[remainder] != i:
                return [i, indexMap[remainder]]
        return []
