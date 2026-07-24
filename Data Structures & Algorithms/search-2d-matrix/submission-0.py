class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False

        n = len(matrix)  #rows(horizontal)
        m = len(matrix[0]) #columns(vertical)

        l=0
        r=n*m-1

        while l<=r:
            mid=(l+r)//2
            mid_val=matrix[mid//m][mid%m]

            if mid_val==target:
                return True
            elif mid_val<target:
                l+=1
            else:
                r-=1
        return False