# Given a square matrix mat, return the sum of the matrix diagonals.

# Only include the sum of all the elements on the primary diagonal and all the elements on the secondary diagonal that are not part of the primary diagonal.

class Solution:
    def diagonalSum(self, mat: list[list[int]]) -> int:
        sum_p, sum_s = 0 , 0
        k = 1
        length = len(mat) 
        si = length // 2 
        sj = length // 2 
        for i in range(len(mat)):
            j=i
            sum_p += mat[i][j]


            if length % 2 == 1:
                  
                if i == si and j == sj :
                    k = k+1
                else:
                    sum_s += mat[i][-k]
                    k = k+1


            else:
                sum_s += mat[i][-k]

                k = k+1
                    
        print( sum_p , sum_s ) 

        total = sum_p + sum_s     

        return total
    



problem = Solution()

mat =       [ [1,1,1,1],
              [1,1,1,1],
              [1,1,1,1],
              [1,1,1,1]    ]

# mat =       [ [1,2,3],
#               [5,5,6],
#               [7,8,9]  ]


# mat = [[5]]
result = problem.diagonalSum(mat)
print(result)
