# An array is monotonic if it is either monotone increasing or monotone decreasing.

# An array nums is monotone increasing if for all i <= j, nums[i] <= nums[j]. An array nums is monotone decreasing if for all i <= j, nums[i] >= nums[j].

# Given an integer array nums, return true if the given array is monotonic, or false otherwise.


class Solution:
    def isMonotonic(self, nums: list[int]) -> bool:

        increasing = decreasing = static= False
        if len(nums) == 1 or len(nums) == 2:
            print(' single element or pair is always monotonic  :)')

            return True        

        for x in range(len(nums)-1):

            if nums[x] == nums[x+1]:
                static = True

            elif nums[x] < nums[x+1]:
                increasing = True
                static = False

            elif nums[x] > nums[x+1]:
                decreasing = True
                static = False

            if decreasing == True and increasing == True :
                break
                

        if decreasing == False and increasing == True and static == False :
            print('Monotonic Increasing')
            return True
        
        elif decreasing == True and increasing == False and static == False:
            print('Monotonic Decreasing ')
            return True
        elif static == True:
            print('Static Monotonic')
            return True
        
        elif decreasing == True and increasing == True  :
            print('NON MONOTONIC')
            return False
        
        else:
            print(':)')

        
        
problem = Solution()
array = [9,2]
result = problem.isMonotonic(array)
print(result)
