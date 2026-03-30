class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        res,l,r = 0, 0, len(people) -1
        while l<=r:
            diff = limit - people[r]
            res+=1
            r-=1
            if l<=r and people[l] <= diff:
                l+=1
        return res
        