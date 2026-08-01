class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = collections.defaultdict(set)
        in_degree = [0] * numCourses
        for course , prereq in prerequisites:
            graph[prereq].add(course)
            in_degree[course] += 1
        visited = set()
        res = []
        queue = deque([i for i in range(numCourses) if in_degree[i] == 0])
        while queue:
            node = queue.popleft()
            if node in visited:
                continue
            res.append(node)
            visited.add(node)
            for nei in graph[node]:
                if nei not in visited:
                    in_degree[nei] -= 1
                    if in_degree[nei] == 0:
                        queue.append(nei)
        return res if len(res) == numCourses else []