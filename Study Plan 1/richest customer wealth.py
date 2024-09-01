# You are given an m x n integer grid accounts where accounts[i][j] is the amount of money the i​​​​​​​​​​​th​​​​ customer has in the j​​​​​​​​​​​th​​​​ bank. Return the wealth that the richest customer has.

# A customer's wealth is the amount of money they have in all their bank accounts. The richest customer is the customer that has the maximum wealth.

class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        wealth_array = []
        
        if accounts == []:
            print('No Account Found :(')
            return 0
        
        else:
            for x in accounts:
                wealth = 0
                for i in range(len(x)):
                    wealth += x[i] 

                wealth_array.append(wealth)

            print(wealth_array)
            richest_customer_wealth = max(wealth_array)

            return richest_customer_wealth
    





problem = Solution()

# accounts = [[2,8,7],[7,1,3],[1,9,5]]
accounts =[[1,5],[7,3],[3,5]]

result = problem.maximumWealth(accounts)
print(result)
