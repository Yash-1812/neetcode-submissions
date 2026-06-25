from collections import defaultdict, deque
from typing import List

class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = defaultdict(list)
        for prereq, course in prerequisites:
            graph[prereq].append(course)
        
        # is_prereq[u][v] will be True if u is a prerequisite of v
        is_prereq = [[False] * numCourses for _ in range(numCourses)]
        
        # Run BFS from each course to map out all reachable courses
        for i in range(numCourses):
            queue = deque([i])
            visited = set([i])
            
            while queue:
                curr = queue.popleft()
                for neighbor in graph[curr]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        is_prereq[i][neighbor] = True
                        queue.append(neighbor)
        
        # Answer each query in O(1) time
        return [is_prereq[u][v] for u, v in queries]
