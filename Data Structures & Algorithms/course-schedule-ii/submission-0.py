class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        visited = set()
        curr_visited = set()
        ret = []

        #lets make the graph through hashmap
        map_ = defaultdict(list)
        for pair in prerequisites:
            map_[pair[0]].append(pair[1])




        def dfs(course):
            if course in curr_visited:
                return True
            
            if course in visited:
                return False

            curr_visited.add(course)

            for prereq in map_[course]:
                if dfs(prereq):
                    return True
            
            visited.add(course)
            curr_visited.discard(course)
            ret.append(course)
            return False
        
        for course in range(numCourses):
            if dfs(course):
                return []
        

        return ret