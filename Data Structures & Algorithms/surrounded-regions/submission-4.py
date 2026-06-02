class Solution:
    def solve(self, board: List[List[str]]) -> None:
        
        hashmap = defaultdict(list)
        
        visited = set()


        def dfs(hash_index, x, y):

            #if we already visited this
            if (x, y) in visited:
                return False
            
            #looking for if out of x margin
            if x >= len(board) or x < 0:
                return True

            #looking to see if in the y margin
            if y >= len(board[0]) or y < 0:
                return True
            
            visited.add((x, y))

            if board[x][y] == "X":
                return False
            
            hashmap[hash_index].append((x, y))

            bool_right = dfs(hash_index, x + 1, y) 
            bool_left = dfs(hash_index, x - 1, y) 
            bool_top = dfs(hash_index, x, y + 1) 
            bool_bottom = dfs(hash_index, x, y - 1)

            if bool_right or bool_left or bool_top or bool_bottom:
                return True
            
            return False
        
        
        count = 0
        for i in range(len(board)):
            for j in range(len(board[0])):
                if (i, j) not in visited and not dfs(count, i, j):
                    for x, y in hashmap[count]:
                        board[x][y] = "X"
                    
                count += 1
        



