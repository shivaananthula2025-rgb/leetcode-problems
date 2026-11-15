class Solution(object):
    def findDegrees(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        n=len(matrix)
        ans=[]
        for i in range(n):
            degree=0
            for j in range(n):
                if matrix[i][j]==1:
                    degree+=1
            ans.append(degree)

        return ans