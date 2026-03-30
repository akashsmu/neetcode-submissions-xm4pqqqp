class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # nums.sort()
        # res = []
        # i = 0 
        # while i < len(nums):
        #     j = i + 1
        #     while j < len(nums) and nums[j] == nums[i]:
        #         j+=1
        #     length = j - i 
        #     if length > len(nums)//3:
        #         res.append(nums[i])
        #     i = j
        # return res

        num1 = num2 = -1
        cnt1 = cnt2 = 0
        for num in nums:
            if num == num1:
                cnt1+=1
            elif num == num2:
                cnt2+=1
            elif cnt1 ==0:
                num1 = num
                cnt1 = 1
            elif cnt2 == 0:
                num2 = num
                cnt2 = 1
            else:
                cnt1 -= 1
                cnt2 -= 1

        cnt1 = cnt2 = 0
        for num in nums:
            if num == num1:
                cnt1 += 1
            elif num == num2:
                cnt2 += 1

        n= len(nums)
        res = []
        if cnt1 > n // 3:
            res.append(num1)
        if cnt2 > n // 3:
            res.append(num2)

        return res
        