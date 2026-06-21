class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = collections.defaultdict(list)
        in_line = [0] * numCourses

        for prereq , course in prerequisites:
            graph[prereq].append(course)
            in_line[course] += 1
        
        queue = deque([i for i in range(numCourses) if in_line[i] == 0])
        taken = 0
        while queue:
            course = queue.popleft()
            taken += 1
            for rem_courses in graph[course]:
                in_line[rem_courses] -= 1
                if in_line[rem_courses] == 0:
                    queue.append(rem_courses)
        return numCourses == taken