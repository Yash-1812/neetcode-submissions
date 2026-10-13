class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = collections.defaultdict(set)
        indegree = [0] * numCourses
        for a , b in prerequisites:
            graph[b].add(a)
            indegree[a] += 1
        res = []
        visited = set()
        queue = deque([i for i in range(numCourses) if indegree[i] == 0])
        while queue:
            node = queue.popleft()
            visited.add(node)
            res.append(node)
            for nei in graph[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    queue.append(nei)
        return res if len(visited) == numCourses else []