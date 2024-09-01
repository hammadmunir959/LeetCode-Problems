# On an infinite plane, a robot initially stands at (0, 0) and faces north. Note that:

# The north direction is the positive direction of the y-axis.
# The south direction is the negative direction of the y-axis.
# The east direction is the positive direction of the x-axis.
# The west direction is the negative direction of the x-axis.
# The robot can receive one of three instructions:

# "G": go straight 1 unit.
# "L": turn 90 degrees to the left (i.e., anti-clockwise direction).
# "R": turn 90 degrees to the right (i.e., clockwise direction).
# The robot performs the instructions given in order, and repeats them forever.

# Return true if and only if there exists a circle in the plane such that the robot never leaves the circle.



# class Solution:
#     def isRobotBounded(self, instructions: str) -> bool:
#         x , y = 0,0 #initial positions
#         step = 1

        # # Directions indicating N, E, S, W respectively
        # directions = [ (0, step) , (step, 0) , (0, -step) , (-step , 0)  ]
        # direction_index = 0
        


        # for i in instructions:
        #     if i == 'G':
        #         # direction of x = dx and direction of y = dy
        #         dx , dy = directions[direction_index]
        #         x += dx
        #         y += dy
        #     elif i == 'L':
        #         direction_index = (direction_index -1) % 4 
        #     elif i == 'R':
        #         direction_index = (direction_index + 1) % 4

            
        # if x == 0 and y == 0 or direction_index != 0 :
        #     return True
        
        # else:
        #     return False







# Solution 2

class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        x , y = 0,0 #initial positions
        step = 1
        Current_direction = 'N'

        for i in instructions:
            if i == 'G' :
                
                if Current_direction == 'N':
                    y += step
                elif Current_direction == 'E':
                    x += step
                elif Current_direction == 'W':
                    x -= step 
                elif Current_direction == 'S':
                    y -= step
                
            elif i == 'L':

                if Current_direction == 'N':
                    Current_direction = 'W'
                elif Current_direction == 'W':
                    Current_direction = 'S'
                elif Current_direction == 'S':
                    Current_direction = 'E'
                elif Current_direction == 'E':
                    Current_direction = 'N'

            elif i == 'R':

                if Current_direction == 'N':
                    Current_direction = 'E'
                elif Current_direction == 'E':
                    Current_direction = 'S'
                elif Current_direction == 'S':
                    Current_direction = 'W'
                elif Current_direction == 'W':
                    Current_direction = 'N'

        print(x,y)
        if (x,y) == (0,0):
            return True
        else:
            return False


problem = Solution()
steps = 'GGLLGG'
result = problem.isRobotBounded(steps)
print(result)
 