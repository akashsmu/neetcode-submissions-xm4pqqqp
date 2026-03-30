class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        # res = max(weights)
        # while True:
        #     ships = 1
        #     cap = res
        #     for w in weights:
        #         if cap - w < 0:
        #             ships += 1
        #             cap = res
        #         cap -= w

        #     if ships <= days:
        #         return res

        #     res += 1

        l,r= max(weights), sum(weights)
        res = r
        def canship(cap):
            ships = 1
            currCap = cap
            for w in weights:
                if currCap - w < 0:
                    ships+=1
                    currCap = cap
                currCap -= w
            
            if ships <= days:
                return True
            return False

        while l <= r:
            mid = (l+r)//2
            if canship(mid):
                res = min(res,mid)
                r = mid - 1
            else:
                l = mid + 1
        return res