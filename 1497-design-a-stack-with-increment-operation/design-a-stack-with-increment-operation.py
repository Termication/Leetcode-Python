class CustomStack:

    def __init__(self, maxSize: int):
        self.stack = []  # To store stack elements
        self.maxSize = maxSize  # Maximum size of the stack
        self.increments = [0] * maxSize  # Store increments for each element
        

    def push(self, x: int) -> None:
        if len(self.stack) < self.maxSize:
            self.stack.append(x)
        

    def pop(self) -> int:
        if not self.stack:
            return -1
        
        idx = len(self.stack) - 1  # Get the top element index
        # Add the accumulated increment to the top element
        result = self.stack.pop() + self.increments[idx]
        
        # Pass the current increment to the next element (if exists)
        if idx > 0:
            self.increments[idx - 1] += self.increments[idx]
        
        # Reset the increment for the current popped element
        self.increments[idx] = 0
        
        return result
        

    def increment(self, k: int, val: int) -> None:
        # Increment the first min(k, len(stack)) elements
        limit = min(k, len(self.stack))
        if limit > 0:
            self.increments[limit - 1] += val


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)