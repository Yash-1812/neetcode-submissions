class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        graph = collections.defaultdict(list)
        in_line = [0] * numCourses

        for course , prereq in prerequisites:
            graph[prereq].append(course)
            in_line[course] += 1
        
        queue = collections.deque([i for i in range(numCourses) if in_line[i] == 0])
        taken = 0

        while queue:
            c = queue.popleft()
            taken += 1
            for nei in graph[c]:
                in_line[nei] -= 1
                if in_line[nei] == 0:
                    queue.append(nei)
        
        return taken == numCourses