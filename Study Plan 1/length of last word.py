# Given a string s consisting of words and spaces, return the length of the last word in the string.

# A word is a maximal  substring  consisting of non-space characters only.


class Solution:
    def lengthOfLastWord(self, s: str) -> int:

        sub_strings = s.split(" ")
        print(sub_strings)

        if sub_strings [-1] != '':
            return len(sub_strings[-1])
        else:
            non_empty = []
            for x in sub_strings:
                if x != '':
                    non_empty.append(x)
        
            last_word = non_empty [-1]
            print(last_word)
            return len(last_word)
        



# Solution # 2

        # index = 0
        # for x in range(len(s)):
        #     if s[x] == " " and x+1 < len(s) and s[x+1] != " " :
        #         index = x  
        
        # last_word = s[index:]
        # last_word = last_word.strip()
        # print(last_word)

        # result = len(last_word)


        # return result
        




problem = Solution()
string = 'Hello Boys,\n This is Leet Code '
result = problem.lengthOfLastWord(string)
print(result)

