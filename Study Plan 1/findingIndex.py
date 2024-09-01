#  Find the Index of the First Occurrence in a String

class Solution:
    def findingSubstring(self, string1, string2) -> int:

        # checking if string2 exists in string1
        try:
            index = string1.index(string2)
            return index
        
        except ValueError :
            return -1



string1 = input("Enter a string 1 : ")
string2 = input('Enter a string 2 : ')        

problem = Solution()

index = problem.findingSubstring(string1 , string2 )

if index == -1:
    print(f" \n {string2} Not found in {string1} ")

else:    
    print(f'index = {index}')


