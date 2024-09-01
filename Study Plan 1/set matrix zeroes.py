# Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.

# You must do it in place.

class Solution:
    def setZeroes(self, matrix: list[list[int]]) :
        """
        Do not return anything, modify matrix in-place instead.
        # """

        r = []
        c = []
        l=0

        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    r.append(i)
                    c.append(j)
                    l += 1
        print()
        for i in range(len(matrix)):
            print(matrix[i])
        print()

        for x in r:
            for y in range( len(matrix[x])):
                matrix[x][y] = 0

        for y in c:
            for x in range( len(matrix)):
                matrix[x][y] = 0


        for i in range(len(matrix)):
            print(matrix[i])

       

problem = Solution()
matrix = [[0,1,2,0],
          [3,6,3,2],
          [8,3,1,3] ]



result = problem.setZeroes(matrix)
# print(result)
