# You are keeping the scores for a baseball game with strange rules. At the beginning of the game, you start with an empty record.

# You are given a list of strings operations, where operations[i] is the ith operation you must apply to the record and is one of the following:

# An integer x.
# Record a new score of x.
# '+'.
# Record a new score that is the sum of the previous two scores.
# 'D' = Record a new score that is the double of the previous score.
# 'C'= Invalidate the previous score, removing it from the record.
# Return the sum of all the scores on the record after applying all the operations.

# The test cases are generated such that the answer and all intermediate calculations fit in a 32-bit integer and that all operations are valid.


class Solution:
    def calPoints(self, ops: list[str]) -> int:
        record : list[int] = []
        score = 0 

        for x in range(len(ops)):
            
            if ops[x] == "C":
                try:
                    record.pop()

                except IndexError as e:                    
                    return score
                    print('Records are empty' , e)

            elif ops[x] == 'D' :
                try:
                    d = record[-1] + record[-1]
                    record.append(d)

                except IndexError as e:                    
                    return score
                    print('Records are empty' ,e)

               

            elif ops[x] == '+':
                try:
                
                    plus = record[-1] + record[-2]
                    record.append(plus)
                except IndexError as e:                    
                    return score
                    print('Records are empty' ,e)

            else:
                try :
                    n = int(ops [x])
                    record.append(n)

                except Exception as e:
                    print(e)

        for x in range(len(record)):
            score = score + record[x]

        print('Total Score = ',score)
              
        return score
        

# ops = ["5","2","C","D","+"]
ops = ['1','D']


problem = Solution()

result = problem.calPoints(ops)
print(result)
