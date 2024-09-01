# For two strings s and t, we say "t divides s" if and only if s = t + t + t + ... + t + t (i.e., t is concatenated with itself one or more times).

# Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.


class Solution:
    def gcd (self, a :int , b:int ) :
        while b != 0:
            a , b= b , a % b

        return a


    def gcdOfStrings(self, str1: str, str2: str) ->str:

        if str1 + str2 != str2 +str1:
            return ""
        else:

            l1 = len(str1)
            l2 = len(str2)

            string_length = self.gcd(l1 , l2)
            string = ""
            string = str1[0 : string_length ]

            return string
    
        
problem = Solution()
str1 = "ABABAB" 
str2 = "ABAB"
print(problem.gcdOfStrings(str1, str2))

        