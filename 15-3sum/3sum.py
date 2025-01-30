class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        Finds all unique triplets in nums that sum to zero.

        Args:
            nums: A list of integers.

        Returns:
            A list of lists of integers, where each inner list represents a triplet.
        """

        result = []
        nums.sort()  # Sort the array to easily handle duplicates and use two pointers

        for i in range(len(nums) - 2):  # Iterate up to the third-to-last element
            if i > 0 and nums[i] == nums[i - 1]:  # Skip duplicate elements for the first number
                continue

            left = i + 1  # Initialize left pointer
            right = len(nums) - 1  # Initialize right pointer

            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]

                if current_sum == 0:
                    result.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1

                    # Skip duplicate elements for the second and third numbers
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

                elif current_sum < 0:
                    left += 1  # Need a larger sum, move left pointer
                else:
                    right -= 1  # Need a smaller sum, move right pointer

        return result