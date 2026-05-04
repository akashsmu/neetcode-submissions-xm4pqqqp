class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        # adj = [[] for _ in range(numCourses)]
        # for crs, pre in prerequisites:
        #     adj[crs].append(pre)
        
        # def dfs(node,target):
        #     if node == target:
        #         return True
        #     for nei in adj[node]:
        #         if dfs(nei, target):
        #             return True
        #     return False


        # res = []
        # for u,v in queries:
        #     res.append(dfs(u,v))
        # return res

        adj = defaultdict(list)
        for prereq, crs in prerequisites:
            adj[crs].append(prereq)

        def dfs(crs):
            if crs not in prereqMap:
                prereqMap[crs] = set()
                for prereq in adj[crs]:
                    prereqMap[crs] |= dfs(prereq)
                prereqMap[crs].add(crs)
                print(crs, prereqMap)
            return prereqMap[crs]

        prereqMap = {}
        for crs in range(numCourses):
            dfs(crs)

        res = []
        for u, v in queries:
            res.append(u in prereqMap[v])
        return res