class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        # Base case: if the expression is a single number, return it as an integer
        if expression.isdigit():
            return [int(expression)]
        
        results = []
        
        # Loop through the expression to find operators
        for i, char in enumerate(expression):
            if char in "+-*":
                # Split the expression into two parts: left and right of the operator
                left_results = self.diffWaysToCompute(expression[:i])
                right_results = self.diffWaysToCompute(expression[i+1:])
                
                # Combine results from both sides based on the current operator
                for left in left_results:
                    for right in right_results:
                        if char == '+':
                            results.append(left + right)
                        elif char == '-':
                            results.append(left - right)
                        elif char == '*':
                            results.append(left * right)
        
        return results