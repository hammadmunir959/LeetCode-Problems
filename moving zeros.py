#  Move Zeroes
# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

# Note that you must do this in-place without making a copy of the array.

 
class Solution:
    def moveZeroes(self, nums ) -> None:
        # Do not return anything, modify nums in-place instead.
        print(f"Before Sorting  {nums}")

        non_zero_index = 0

        for x in nums:
            if x  != 0:
                nums[non_zero_index] = x
                non_zero_index += 1

        for x in range(non_zero_index ,len(nums) ):
            nums [x] = 0

        print(f"After Sorting  {nums}")


given_list = [1,2,7,5,3,0,7,0,3,0,5,8,0,6,3,7,8]
problem = Solution()

problem.moveZeroes(given_list)