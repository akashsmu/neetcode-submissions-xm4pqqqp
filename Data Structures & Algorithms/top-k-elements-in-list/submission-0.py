class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        for num in nums:
            count[num] = count[num] + 1
        
        maxValues = sorted(list(count.values()), reverse=True)[:k]
        out = []
        for key, value in count.items():
            if k != 0 and value in maxValues:
                out.append(key)
                k-=1

        return out

