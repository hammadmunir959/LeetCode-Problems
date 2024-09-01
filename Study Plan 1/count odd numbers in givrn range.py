# Given two non-negative integers low and high. Return the count of odd numbers between low and high (inclusive).

# class Solution:

    # def countOdds(self, low: int, high: int) -> int:
    #     count = 0
    #     for x in range(low , high +1 ):
            
    #         if x % 2 !=0 :
    #             count += 1 
    
    #     return count
    

# Optimal Solution
class Solution:
    def countOdds(self, low: int, high: int) -> int:
        count = 0
        n = high - low

        count = n // 2 

        if (low % 2 !=0) or (high % 2 != 0) :
            count += 1

        
        return count




problem = Solution()
start = 8
end  =  10
result = problem.countOdds(start, end)
print("Number of Odds in Given range is : " ,result)