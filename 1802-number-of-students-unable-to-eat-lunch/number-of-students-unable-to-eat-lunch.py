class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        # Initialize a counter to keep track of how many times we've gone through the queue without success
        attempts = 0

        # While there are still students in the queue
        while students:
            # If the front student can take the top sandwich
            if students[0] == sandwiches[0]:
                # Remove both the student and the sandwich
                students.pop(0)
                sandwiches.pop(0)
                # Reset the counter since a student successfully took a sandwich
                attempts = 0
            else:
                # Move the student to the end of the queue
                students.append(students.pop(0))
                # Increment the counter for an unsuccessful attempt
                attempts += 1

            # If we've attempted as many times as there are students, no one can eat the top sandwich
            if attempts == len(students):
                break

        # The number of students left in the queue is the number unable to eat
        return len(students)
        