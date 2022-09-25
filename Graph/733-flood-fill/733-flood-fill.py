from collections import deque

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        num_rows, num_cols = len(image), len(image[0])
        def get_neighbors(coord, color):
            row, col = coord
            DELTA_ROW = [-1, 0, 1, 0]
            DELTA_COL = [0, 1, 0, -1]
            for i in range(len(DELTA_ROW)):
                neighbor_row = row + DELTA_ROW[i]
                neighbor_col = col + DELTA_COL[i]
                if 0 <= neighbor_row < num_rows and 0 <= neighbor_col < num_cols:
                    if image[neighbor_row][neighbor_col] == color:
                        yield neighbor_row, neighbor_col
        
        def bfs(root):
            q = deque([root])
            visited = [ [False for _ in range(num_cols)] for _ in range(num_rows)]
            r, c = root
            current_color = image[r][c]
            image[r][c] = color
            visited[r][c] = True
            
            while len(q) > 0:
                node = q.popleft()
                for neighbor in get_neighbors(node, current_color):
                    r, c = neighbor
                    if visited[r][c]:
                        continue
                    image[r][c] = color
                    q.append(neighbor)
                    visited[r][c] = True
        bfs((sr,sc))
        return image
                
            
            
        