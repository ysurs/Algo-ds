You are given an m x n integer matrix matrix with the following two properties:

1.Each row is sorted in non-decreasing order.
2.The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        n_rows=len(matrix)
        n_colmns=len(matrix[0])

        row_first=0
        row_last=n_rows-1

        target_row=-1
        while row_first<=row_last:
            mid=(row_first+row_last)//2
            if target>=matrix[mid][0] and target<=matrix[mid][n_colmns-1]:
                target_row=mid
                break
            elif target<matrix[mid][0]:
                row_last=mid-1
            
            else:
                row_first=mid+1

        if target_row==-1:
            return False

        left=0
        right=n_colmns-1

        while left<=right:

            mid=(left+right)//2

            if matrix[target_row][mid]==target:
                return True
            
            elif matrix[target_row][mid]>target:
                right=mid-1
            else:
                left=mid+1
        
            
        return False
    

1. We will use the property: if we have a an array which is sorted and we need to find an element, we should use binary search
2. We will use property 2 given above to find the target row using binary search
3. after we find it, we perform binary search again to find the element.