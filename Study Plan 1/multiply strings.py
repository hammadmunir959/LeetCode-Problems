# Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.

# Note: You must not use any built-in BigInteger library or convert the inputs to integer directly.
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        l_1 = len(num1)
        l_2 = len(num2)
        
        # Initialize the product array with zeros
        product = [0] * (l_1 + l_2)
        
        # Reverse iterating over each digit in num2
        for i in range(l_2 - 1, -1, -1):
            dig1 = int(num2[i])
            carry = 0
            
            # Reverse iterating over each digit in num1
            for j in range(l_1 - 1, -1, -1):
                dig2 = int(num1[j])
                
                # Calculate the positions in the product array
                pos1 = i + j + 1
                pos2 = i + j
                
                # Multiply the digits and add the current value and carry
                total = dig1 * dig2 + product[pos1] + carry
                product[pos1] = total % 10
                carry = total // 10
            
            # Add any remaining carry
            product[pos2] += carry
        
        # Convert product list to string and strip leading zeros
        result = ''.join(map(str, product)).lstrip('0')
        
        # Return result or '0' if the result is empty
        return result if result else '0'

# Example usage
problem = Solution()
num1 = '123'
num2 = '456'
result = problem.multiply(num1, num2)
print(result)  # Output: "56088"
