class Solution:
    def countLargestGroup(self, n: int) -> int:
        def sum_digits(num):
            s = 0
            while num:
                s += num % 10
                num //= 10
            return s

        group_counts = collections.defaultdict(int)
        for i in range(1, n + 1):
            digit_sum = sum_digits(i)
            group_counts[digit_sum] += 1

        max_size = 0
        for count in group_counts.values():
            max_size = max(max_size, count)

        largest_group_count = 0
        for count in group_counts.values():
            if count == max_size:
                largest_group_count += 1

        return largest_group_count