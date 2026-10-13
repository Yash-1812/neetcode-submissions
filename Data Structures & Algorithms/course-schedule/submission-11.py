class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = collections.defaultdict(set)
        indegree = [0] * numCourses
        for a , b in prerequisites:
            graph[b].add(a)
            indegree[a] += 1
        queue = deque([i for i in range(numCourses) if indegree[i] == 0])
        visited = set()
        while queue:
            node = queue.popleft()
            visited.add(node)
            for nei in graph[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    queue.append(nei)
                    visited.add(nei)
        return True if len(visited) == numCourses else False