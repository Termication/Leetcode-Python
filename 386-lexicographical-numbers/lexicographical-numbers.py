class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        result = []
        num = 1
        
        for _ in range(n):
            result.append(num)
            
            # Try to go deeper in the tree (multiply by 10)
            if num * 10 <= n:
                num *= 10
            else:
                # Increment the number, handling cases where it ends in 9 or exceeds n
                while num % 10 == 9 or num + 1 > n:
                    num //= 10
                num += 1
                
        return result