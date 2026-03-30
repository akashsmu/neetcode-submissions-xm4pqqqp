class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        # trips.sort(key=lambda x:x[1])
        # for i in range(len(trips)):
        #     curPass = trips[i][0]
        #     for j in range(i+1,len(trips)):
        #         if trips[j][1] < trips[i][2]:
        #             curPass += trips[j][0]
        #     if curPass > capacity:
        #         return False 
        # return True

        # trips.sort(key=lambda t: t[1])
        # minHeap = []
        # currPass = 0
        # for numPas, start,end in trips:
        #     while minHeap and minHeap[0][0] <= start:
        #         currPass -= heapq.heappop(minHeap)[1]
            
        #     currPass += numPas
        #     if currPass > capacity:
        #         return False
            
        #     heapq.heappush(minHeap, [end,numPas])
        # return True

        points = []
        for pas, start,end in trips:
            points.append([start,pas])
            points.append([end,-pas])
        
        points.sort()
        curPas = 0
        for point, pas in points:
            curPas += pas
            if curPas > capacity:
                return False
        return True