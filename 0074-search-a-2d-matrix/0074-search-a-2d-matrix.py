class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = 0
        for i in range(len(matrix)):
            if target <= matrix[i][-1] and target >= matrix[i][0]:
                row = i
                break
        else:
            return False
        
        high = len(matrix[row]) - 1
        low = 0

        while low <= high:
            mid = (high + low) // 2

            if matrix[row][mid] == target:
                return True
            elif target > matrix[row][mid]:
                low = mid + 1
            else:
                high = mid - 1
        return False
            
        


        