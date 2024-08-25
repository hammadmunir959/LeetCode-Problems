# 1822. Sign of the Product of an Array

# There is a function signFunc(x) that returns:

# 1 if x is positive.
# -1 if x is negative.
# 0 if x is equal to 0.
# You are given an integer array nums. Let product be the product of all values in the array nums.

# Return signFunc(product).


class Solution:

    def arraySign(self, nums: list[int]) -> int:
        
        product = 1
        for x in range(len(nums)):
        
            product = nums[x] * product

        self.signFunc(product)
        
        return self.signFunc(product)

    def signFunc(self, product):
            if product == 0:
                return 0
            elif product > 0:
                return 1
            else:
                return -1
            


problem = Solution()
num1 = [1,2,4,-3,7,-7,5,9,-4 -2]
num2 = [1,2,4,5,77,5]
num3 = [1,2,4,5,77,5,0]

result = problem.arraySign(num1)
print(result)

result = problem.arraySign(num2)
print(result)

result = problem.arraySign(num3)
print(result)
