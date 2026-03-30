class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows,cols = len(grid), len(grid[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        INF = 2147483647

        def bfs(r,c):
            q = deque([(r,c)])
            visit = [[False] * cols for _ in range(rows)]
            visit[r][c] = True
            res = 0
            while q:
                for _ in range(len(q)):
                    r,c = q.popleft()
                    if grid[r][c] == 0: return res
                    for dr, dc in directions:
                        nr,nc = r + dr, c + dc
                        if (0 <= nr < rows and 0 <= nc < cols and not visit[nr][nc] and grid[nr][nc] != -1):
                            q.append((nr,nc))
                            visit[nr][nc] = True
                res += 1
            return INF
                


        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == INF:
                    grid[r][c] = bfs(r,c)