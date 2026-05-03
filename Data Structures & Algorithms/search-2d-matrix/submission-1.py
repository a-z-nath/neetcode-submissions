class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # first find row where it might be 0 to m-1
        # find on that row if the column exist

        def findRow(mat: List[List[int]], target):
            row = len(mat)
            low, high = 0, row -1
            ans = 0
            while low <= high:
                mid = (low + high) // 2
                if target == mat[mid][0]:
                    return mid
                if target > mat[mid][0]:
                    ans = mid
                    low = mid + 1
                else:
                    high = mid - 1
            return ans
        
        def findCol(mat: List[List[int]], row: int, target: int):
            col = len(mat[0])
            low, high = 0, col - 1
            while low <= high:
                mid = (low + high) // 2
                if target == mat[row][mid]:
                    return mid
                if target < mat[row][mid]:
                    high = mid - 1
                else:
                    low = mid+1
            
            return -1

        row = findRow(matrix, target)
        print(row)
        col = findCol(matrix, row, target)

        return True if col != -1 else False