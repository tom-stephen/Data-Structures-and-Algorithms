class DFS:

    @staticmethod
    def dfs(graph, start):
        visited = set()
        DFS.dfs_helper(graph, start, visited)

    @staticmethod
    def dfs_helper(graph, node, visited):
        visited.add(node)
        print(node, end=' ')
        for neighbor in graph[node]:
            if neighbor not in visited:
                DFS.dfs_helper(graph, neighbor, visited)
