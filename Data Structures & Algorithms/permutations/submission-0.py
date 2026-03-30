class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # perms = [[]]
        # for num in nums:
        #     new = []
        #     for p in perms:
        #         for i in range(len(p)+1):
        #             pCopy= p.copy()
        #             pCopy.insert(i,num)
        #             new.append(pCopy)
        #     perms = new
        # return perms

        self.res = []
        self.backtrack([],nums,[False]*len(nums))
        return self.res
    
    def backtrack(self,perm,nums,pick):
        if len(perm) == len(nums):
            self.res.append(perm.copy())
            return
        
        for i in range(len(nums)):
            if not pick[i]:
                perm.append(nums[i])
                pick[i] = True
                self.backtrack(perm,nums,pick)
                perm.pop()
                pick[i] = False
        