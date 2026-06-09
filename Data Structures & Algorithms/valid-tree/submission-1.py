class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        visited = set()

        graph = defaultdict(list)

        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])

        def dfs(prev, curr):
            if curr in visited:
                return True  #true means that there is a cycle
            
            visited.add(curr)

            for neighor in graph[curr]:
                if neighor == prev:
                    continue

                if dfs(curr, neighor):
                    return True
            
            return False
                
        

        visited.add(0)

        for neighor in graph[0]:
            if dfs(0, neighor):
                return False
        
        if len(visited) != n:
            return False 
            
        return True
        
        