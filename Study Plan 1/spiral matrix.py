# Given an m x n matrix, return all elements of the matrix in spiral order.

class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        result: list[int] = []

        # boundaries
        bottom = len(matrix) - 1
        right = len(matrix[0]) - 1
        top = 0
        left = 0

        while top <= bottom and left <= right:

            # Traversing from left to right along the top row

            for i in range(left, right + 1):
                result.append(matrix[top][i])
            top += 1  # Moving top boundary down

            # Traversing from top to bottom along the right 
            
            for i in range(top, bottom + 1):
                result.append(matrix[i][right])
                
            right -= 1  # Moving the right boundary left

            # Traversing from right to left along the bottom row (if still within bounds)
            if top <= bottom:
                for i in range(right, left - 1, -1):
                    result.append(matrix[bottom][i])
                bottom -= 1  # Moving the bottom boundary up

            # Traversing from bottom to top along the left column (if still within bounds)
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    result.append(matrix[i][left])
                left += 1  # Moving the left boundary right

        return result


# Example usage
problem = Solution()
matrix = [
    [1, 2, 3, 6],
    [4, 5, 6, 3],
    [7, 8, 9, 0],
    [4, 5, 6, 3]
]

result = problem.spiralOrder(matrix)
print(result)
