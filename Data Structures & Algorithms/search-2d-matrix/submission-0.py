class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        columns = len(matrix[0])
        l,r = 0,rows*columns - 1

        while l <= r:
            mid = (l+r)//2 #6 rows 3 c 4
            midel = matrix[mid//columns][mid%columns]
            if midel == target:
                return True
            elif midel < target:
                l = mid+1
            else:
                r = mid-1
        return False

