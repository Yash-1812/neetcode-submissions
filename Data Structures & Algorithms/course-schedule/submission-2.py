class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {i: [] for i in range(numCourses)}
        
        for a, b in prerequisites:
            graph[b].append(a)   # b → a
        
        visited = set()
        path = set()

        def dfs(node):
            if node in path:
                return False   # cycle detected
            if node in visited:
                return True    # already processed
            
            path.add(node)
            
            for nei in graph[node]:
                if not dfs(nei):
                    return False
            
            path.remove(node)
            visited.add(node)
            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return False
        
        return True