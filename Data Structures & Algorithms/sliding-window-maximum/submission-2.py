class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # res = []
        # for i in range(len(nums)-k+1):
        #     arr = nums[i:i+k]
        #     res.append(max(arr))
        # return res

        # heap = []
        # res = []
        # for i in range(len(nums)):
        #     heapq.heappush(heap,(-nums[i],i))
        #     if i+1 >= k:
        #         while heap[0][1] <= i - k:
        #             heapq.heappop(heap)
        #         res.append(-heap[0][0])
        # return res

        n = len(nums)
        leftMax = [0] * n
        rightMax = [0] * n

        leftMax[0] = nums[0]
        rightMax[n - 1] = nums[n - 1]

        for i in range(1, n):
            if i % k == 0:
                leftMax[i] = nums[i]
            else:
                leftMax[i] = max(leftMax[i - 1], nums[i])

            if (n - 1 - i) % k == 0:
                rightMax[n - 1 - i] = nums[n - 1 - i]
            else:
                rightMax[n - 1 - i] = max(rightMax[n - i], nums[n - 1 - i])
        
        #print(leftMax, rightMax)
        res = [0] * (n-k+1)
        for i in range(n-k+1):
            res[i] = max(rightMax[i],leftMax[i+k-1])
        return res