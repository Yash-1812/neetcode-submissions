class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if not prerequisites:
            return True
        graph = collections.defaultdict(list)
        in_courses = [0] * numCourses
        for prereq , course in prerequisites:
            graph[prereq].append(course)
            in_courses[course] += 1
        
        queue = deque([i for i in range(numCourses) if in_courses[i] == 0])
        taken = 0
        while queue:
            c = queue.popleft()
            taken += 1
            for courses in graph[c]:
                in_courses[courses] -= 1
                if in_courses[courses] == 0:
                    queue.append(courses)
        return taken == numCourses