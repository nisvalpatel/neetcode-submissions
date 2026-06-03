class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        visiting = set()

        def dfs(x, y, word_index):

            if word_index >= len(word) or (x,y) in visiting:
                return False
            
            if x >= len(board) or x < 0:
                return False
            
            if y >= len(board[0]) or y < 0:
                return False
            
            if board[x][y] != word[word_index]:
                return False
            
            if word_index == len(word) - 1:
                return True

            visiting.add((x,y))

            if dfs(x+1, y, word_index + 1) or dfs(x-1, y, word_index + 1) or dfs(x, y-1, word_index + 1) or dfs(x, y+1, word_index + 1):
                visiting.remove((x,y))
                return True
            
            visiting.remove((x,y))
            return False

        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(i, j, 0):
                    return True
        
        return False


            

