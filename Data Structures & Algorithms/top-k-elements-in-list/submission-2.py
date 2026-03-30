class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # count = defaultdict(int)
        # for num in nums:
        #     count[num] = count[num] + 1
        
        # maxValues = sorted(list(count.values()), reverse=True)[:k]
        # out = []
        # for key, value in count.items():
        #     if k != 0 and value in maxValues:
        #         out.append(key)
        #         k-=1

        # return out

        ############ Heap #############
        # count = defaultdict(int)
        # for num in nums:
        #     count[num] = count[num] + 1

        # heap = []
        # for key, cnt in count.items():
        #     heapq.heappush(heap, (cnt, key))
        #     if len(heap) > k:
        #         heapq.heappop(heap)
        
        # res = []
        # while heap:
        #     res.append(heapq.heappop(heap)[1])
        # return res


        ############ BUCKET SORT ################
        count = defaultdict(int)
        freq = [[] for i in range(len(nums) + 1)]
        for num in nums:
            count[num] = count[num] + 1
        for key,value in count.items():
            freq[value].append(key)
        
        res = []
        for i in range(len(freq)-1,0,-1):
            for num in freq[i]:
                res.append(num)
                if len(res) ==k:
                    return res
            

        







