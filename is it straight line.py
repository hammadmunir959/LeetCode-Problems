# You are given an array coordinates, coordinates[i] = [x, y], where [x, y] represents the coordinate of a point. Check if these points make a straight line in the XY plane.

class Solution:
    def checkStraightLine(self, c: list[list[int]]) -> bool:
        # straightline = y = mx+b

        x1,y1 = c[0]
        x2 , y2 = c[1]

        ay = y2 - y1
        ax = x2 - x1


        for i in range( 2, len(c)):
            x2,y2 = c[i]

            py = y2 - y1
            px = x2 - x1

            if ax * py != ay * px:
                return False

        return True



problem = Solution()
coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
result = problem.checkStraightLine(coordinates)
print(result)  # Output: "56088"
