class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])

        # find row, find value in that row, if find return
        top, bot = 0, ROWS - 1
        while top <= bot:
            row = (top + bot) // 2
            if matrix[row][-1] < target:
                top = row + 1
            elif matrix[row][0] > target:
                bot = row - 1
            else:
                break
        if not (top <= bot):
            return False
        row = (top + bot) // 2
        l, h = 0, COLS - 1
        while l <= h:
            col = (l + h) // 2
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                l = col + 1
            else:
                h = col - 1

        return False