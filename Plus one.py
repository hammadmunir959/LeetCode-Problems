class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        print(digits)

        last_digit = digits[-1]

        if  last_digit != 9:
        
            updated_last_digit = digits[-1]
            updated_last_digit += 1
            print(" Updated last digit = ", updated_last_digit)

            digits[-1] = updated_last_digit

            return digits

        
        else:
            
            stringed_list = "".join(map(str,digits))

            new_list = int(stringed_list)

# adding 0ne in the larger number
            new_list += 1

            result = [] 

            while new_list > 0 :

                num =new_list % 10 
                result.append(num)
                new_list = new_list // 10

            result = result[-1::-1]

            return result


problem = Solution()

digits : list[int] = [2,1 ,3,4 ,9,9,9]

updated_digits = problem.plusOne(digits)

print(updated_digits)