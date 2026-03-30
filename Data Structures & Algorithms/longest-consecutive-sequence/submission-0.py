class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # res = 0
        # store = set(nums)

        # for num in nums:
        #     streak,curr = 0, num
        #     while curr in store:
        #         streak+=1
        #         curr+=1
            
        #     res = max(res,streak)
        
        # return res

        # if not nums:
        #     return 0
        
        # res = 0
        # nums.sort()
        # streak, curr = 0, nums[0]
        # i = 0
        # while i < len(nums):
        #     if curr != nums[i]:
        #         curr = nums[i]
        #         streak = 0
        #     while i < len(nums) and curr == nums[i]:
        #         i+=1
        #     streak+=1
        #     curr += 1
        #     res = max(res,streak)
        # return res


        numSet = set(nums)
        longest = 0
        for num in numSet:
            if (num - 1) not in numSet:
                length = 1
                while num + length in numSet:
                    length += 1
                longest = max(longest,length)
        return longest

            