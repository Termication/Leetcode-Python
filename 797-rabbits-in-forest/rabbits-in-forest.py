class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        """
        Calculates the minimum number of rabbits in the forest.

        Args:
            answers: A list where answers[i] is the answer of the ith rabbit.

        Returns:
            The minimum possible number of rabbits in the forest.
        """
        counts = collections.Counter(answers) # Count frequencies of each answer
        total_rabbits = 0

        for x, count_x in counts.items():
            # x is the answer given by count_x rabbits
            # Each group for answer x has size x + 1
            group_size = x + 1

            # Calculate the number of groups needed for these count_x rabbits
            # Each group can accommodate 'group_size' rabbits answering 'x'
            # We need ceil(count_x / group_size) groups
            num_groups = math.ceil(count_x / group_size)
            # Alternative using integer division:
            # num_groups = (count_x + group_size - 1) // group_size

            # Each group contributes group_size rabbits to the total minimum
            total_rabbits += num_groups * group_size

        return int(total_rabbits) # Ensure result is integer
        