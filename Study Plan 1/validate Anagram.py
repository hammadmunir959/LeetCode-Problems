# Anagram is  A word or phrase that is created by rearranging the letters of another word or phrase.

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s = sorted(s)
        t = sorted(t)

        if s == t :
            return True
        else:
            return False
        

string1 = input('Enter string #1 : ')
string2 = input('Enter string #2 : ')


problem = Solution()

result = problem.isAnagram(string1 , string2)

print(result)