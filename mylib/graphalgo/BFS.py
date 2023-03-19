from collections import deque

class BFS:

    @staticmethod
    def bfs(graph, start):
        visited = []
        queue = deque([start])
        while queue:
            node = queue.popleft()
            if node not in visited:
                visited.append(node)
                neighbors = graph.get(node, [])
                for neighbor in neighbors:
                    if neighbor not in visited:
                        queue.append(neighbor)
        return visited