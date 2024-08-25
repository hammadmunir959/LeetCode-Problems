# Given a string s, check if it can be constructed by taking a substring of it and appending multiple copies of the substring together.

class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        t = s + s
        t = t [1 : -1]

        if s in t :
            return True
        else:
            return False


string1 = 'abab'

problem = Solution()

result = problem.repeatedSubstringPattern(string1)

print(result)
