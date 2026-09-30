class Solution:
    def validPath(self, n, edges, source, destination):

        # Create adjacency list
        graph = [[] for _ in range(n)]

        # Build graph
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        # Keep track of visited nodes
        visited = [False] * n

        def dfs(node):

            # If destination is reached
            if node == destination:
                return True

            # Mark current node as visited
            visited[node] = True

            # Visit all neighbours
            for neighbour in graph[node]:

                if not visited[neighbour]:

                    if dfs(neighbour):
                        return True

            return False

        return dfs(source)