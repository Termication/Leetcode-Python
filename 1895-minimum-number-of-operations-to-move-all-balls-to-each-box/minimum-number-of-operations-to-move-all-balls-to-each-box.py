class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        answer = [0] * n
        left_balls, left_ops = 0, 0
        right_balls, right_ops = 0, 0
        # Calculate right_balls and right_ops initially
        for i in range(n):
            if boxes[i] == '1':
                right_balls += 1
                right_ops += i

        for i in range(n):
            # Add operations for current box
            answer[i] = left_ops + right_ops

            # Update left_balls, right_balls, left_ops, and right_ops
            if boxes[i] == '1':
                left_balls += 1
                right_balls -= 1
            left_ops += left_balls
            right_ops -= right_balls

        return answer