class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        graph = collections.defaultdict(set)
        in_degree = [0] * numCourses
        visited = set()
        for course , prereq in prerequisites:
            graph[prereq].add(course)
            in_degree[course] += 1
        queue = deque([i for i in range(numCourses) if in_degree[i] == 0])
        while queue:
            node = queue.popleft()
            visited.add(node)
            for nei in graph[node]:
                in_degree[nei] -= 1
                if in_degree[nei] == 0:
                    queue.append(nei)
        return True if len(visited) == numCourses else False