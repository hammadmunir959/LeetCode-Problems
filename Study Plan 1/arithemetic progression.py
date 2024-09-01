

class Solution:
    def canMakeArithmeticProgression(self, arr: list[int]) -> bool:
        arr = sorted(arr)

        n = arr[1] - arr[0]
        print(n)

        for x in range(0,len(arr)-1):

            m = arr[x+1] - arr[x]
            if m != n :
                return False
        
        return True

            


problem = Solution()
arr1 = [3,5,1]
arr2 = [1,2,4]

# result = problem.canMakeArithmeticProgression(arr1)
# print(result)


result = problem.canMakeArithmeticProgression(arr2)
print(result)