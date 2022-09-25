class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        num_rows = len(grid)
        num_cols = len(grid[0])
        
        def get_neighbors(coord):
            res = []
            row, col = coord
            delta_row = [-1, 0, 1, 0]
            delta_col = [0, 1, 0, -1]
            for i in range(len(delta_row)):
                r = row + delta_row[i]
                c = col + delta_col[i]
                if 0 <= r < num_rows and 0 <= c < num_cols:
                    res.append((r, c))
            return res
        
        def bfs(start):
            q = deque([start])
            r, c = start
            grid[r][c] = "0"
            while len(q) > 0:
                node = q.popleft()
                for neighbor in get_neighbors(node):
                    r, c = neighbor
                    if grid[r][c] == "0":
                        continue
                    q.append(neighbor)
                    grid[r][c] = "0"
        
        count = 0
        for r in range(num_rows):
            for c in range(num_cols):
                if grid[r][c] == "0":
                    continue
                bfs((r, c))
                count += 1
        return count