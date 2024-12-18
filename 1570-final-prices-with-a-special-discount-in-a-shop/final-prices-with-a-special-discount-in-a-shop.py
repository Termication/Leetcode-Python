class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        """
        Calculates the final prices with a special discount in a shop.

        Args:
            prices (List[int]): List of item prices.

        Returns:
            List[int]: Final prices after applying discounts.
        """
        n = len(prices)
        result = prices[:]  # Initialize result with the original prices
        stack = []  # Monotonic stack to track indices
        
        for i in range(n):
            # While stack is not empty and current price <= price at stack's top
            while stack and prices[i] <= prices[stack[-1]]:
                index = stack.pop()
                result[index] -= prices[i]  # Apply the discount
            
            stack.append(i)  # Push the current index onto the stack
        
        return result
        