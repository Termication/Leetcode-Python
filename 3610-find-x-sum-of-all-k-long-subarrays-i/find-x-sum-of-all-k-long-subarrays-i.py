from collections import defaultdict

class Solution(object):
    def findXSum(self, nums, k, x):
        """
        :type nums: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        n = len(nums)
        result = []
        
        # Frequency counter for current window
        freq = defaultdict(int)
        
        # Initialize first window
        for i in range(k):
            freq[nums[i]] += 1
        
        # Process each window
        for i in range(n - k + 1):
            # Calculate x-sum for current window
            if len(freq) <= x:
                # If fewer distinct elements than x, sum all elements
                total = sum(nums[i:i+k])
            else:
                # Sort elements by frequency then value
                elements = list(freq.keys())
                elements.sort(key=lambda num: (-freq[num], -num))
                
                # Take top x elements
                top_x = elements[:x]
                
                # Sum all occurrences of top x elements
                total = 0
                for num in top_x:
                    total += num * freq[num]
            
            result.append(total)
            
            # Slide window (unless at last position)
            if i < n - k:
                # Remove leftmost element
                left_num = nums[i]
                freq[left_num] -= 1
                if freq[left_num] == 0:
                    del freq[left_num]
                
                # Add rightmost element  
                right_num = nums[i + k]
                freq[right_num] += 1
        
        return result
        