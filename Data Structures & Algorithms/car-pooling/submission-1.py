class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key=lambda x:x[1])
        for i in range(len(trips)):
            curPass = trips[i][0]
            for j in range(i+1,len(trips)):
                if trips[j][1] < trips[i][2]:
                    curPass += trips[j][0]
            if curPass > capacity:
                return False 
        return True