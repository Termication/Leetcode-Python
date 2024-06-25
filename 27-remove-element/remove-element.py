class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # Pointer for the next position to place the non-val element
        k = 0
        
        # Iterate over all elements in the array
        for i in range(len(nums)):
            # If the current element is not equal to val, place it at the k-th position
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
                
        return k