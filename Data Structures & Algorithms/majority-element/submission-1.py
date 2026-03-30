class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # count = {}
        # for num in nums:
        #     count[num] = count.get(num, 0 ) + 1
        
        # return max(count, key = count.get)

        count = 1 
        countNum = nums[0]

        for num in nums[1:]:
            if num == countNum:
                count += 1
            elif num != countNum and count != 0:
                count -= 1
            elif num != countNum and count == 0:
                countNum = num
                count = 1
        
        return countNum
            