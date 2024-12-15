class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        """
        Calculate the maximum average pass ratio after assigning extra students.

        Args:
            classes (list[list[int]]): List of [pass, total] for each class.
            extraStudents (int): Number of extra students to assign.

        Returns:
            float: Maximum average pass ratio.
        """
        # Function to compute delta (improvement by adding one student)
        def delta(pass_students, total_students):
            return (pass_students + 1) / (total_students + 1) - (pass_students / total_students)

        # Max-heap to store (-delta, pass_students, total_students) for each class
        heap = []
        for pass_students, total_students in classes:
            heapq.heappush(heap, (-delta(pass_students, total_students), pass_students, total_students))

        # Assign extra students
        for _ in range(extraStudents):
            # Pop the class with the maximum delta
            max_delta, pass_students, total_students = heapq.heappop(heap)
            pass_students += 1
            total_students += 1
            # Push updated values back into the heap
            heapq.heappush(heap, (-delta(pass_students, total_students), pass_students, total_students))

        # Calculate the final average pass ratio
        total_ratio = 0
        for _, pass_students, total_students in heap:
            total_ratio += pass_students / total_students

        return total_ratio / len(classes)
        