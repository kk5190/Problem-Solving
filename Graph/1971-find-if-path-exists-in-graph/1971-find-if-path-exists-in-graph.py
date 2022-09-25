from collections import deque
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = {}
        for edge in edges:
            graph[edge[0]] = graph.get(edge[0], []) + [edge[1]]
            graph[edge[1]] = graph.get(edge[1], []) + [edge[0]]
        
        q, visited = deque(), set()
        q.append(source)
        visited.add(source)
        
        while len(q) > 0:
            node = q.popleft()
            if node == destination:
                return True
            for neighbor in graph[node]:
                if neighbor not in visited:
                    q.append(neighbor)
                    visited.add(neighbor)
        return False
        