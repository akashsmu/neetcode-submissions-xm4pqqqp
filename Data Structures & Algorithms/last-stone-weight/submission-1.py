class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones.sort()
        while len(stones) > 1:
            x,y = stones.pop(), stones.pop()
            if x == y:
                continue
            else:
                stones.append(abs(x-y))
                stones.sort()
        
        return stones[0] if len(stones) else 0