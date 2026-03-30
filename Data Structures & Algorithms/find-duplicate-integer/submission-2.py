class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # count = Counter(nums)
        # for num in range(len(nums)+1):
        #     if count[num] > 1:
        #         return num
        # seen = set()
        # for num in nums:
        #     if num in seen:
        #         return num
        #     seen.add(num)

        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow
        
