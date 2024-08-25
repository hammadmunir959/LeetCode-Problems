class Solution:
    def romanToInt(self, s: str) -> int:
        print(s)
        roman = {
            
            "I" : 1,
            "V"  : 5,
            "X" : 10,
            "L"  : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000
            
                  }
        
        result = 0

        for x in range(len(s)):
            value = roman[s[x]]

            if x+1 < len(s) and  value < roman[s[x+1]]:
                result = result - value
            else:
                result = result + value
            
        return result








problem = Solution()
roman = 'MCDLIX'
result = problem.romanToInt(roman)
print(result)

