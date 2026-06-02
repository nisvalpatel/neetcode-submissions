class Solution:
    def canFinish(self, numCourses, prerequisites):
        # Step 1: build graph
        graph = {i: [] for i in range(numCourses)}
        for a, b in prerequisites:
            graph[b].append(a)  # b → a

        # Step 2: visit states
        # 0 = unvisited, 1 = visiting, 2 = visited
        visit = [0] * numCourses

        # Step 3: DFS
        def dfs(course):
            if visit[course] == 1:
                return False  # cycle detected
            if visit[course] == 2:
                return True   # already processed

            visit[course] = 1  # mark as visiting

            for neighbor in graph[course]:
                if not dfs(neighbor):
                    return False

            visit[course] = 2  # mark as visited
            return True

        # Step 4: check all courses
        for course in range(numCourses):
            if not dfs(course):
                return False

        return True