class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n, m = len(matrix), len(matrix[0])
        for i in range(n):
            for j in range(i, m):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        print(matrix)
        for i in range(n):
            for j in range(m//2):
                matrix[i][j], matrix[i][m - j - 1] =  matrix[i][m - j - 1], matrix[i][j]