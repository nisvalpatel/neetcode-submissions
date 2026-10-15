class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        arr = [[0] * (len(text1) + 1) for _ in range(len(text2) + 1)]

        for i in range(len(text2) - 1, -1, -1):
            for j in range(len(text1) - 1, -1, -1):
                
                if text2[i] == text1[j]:
                    arr[i][j] = max(arr[i + 1][j + 1] + 1, arr[i][j + 1], arr[i + 1][j])
                else:
                    arr[i][j] = max(arr[i][j + 1], arr[i + 1][j])
                
        return arr[0][0]
