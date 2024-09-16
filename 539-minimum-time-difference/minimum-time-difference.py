class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        # Convert time points to minutes
        def convertToMinutes(time):
            hours, minutes = map(int, time.split(':'))
            return hours * 60 + minutes
        
        # Convert all time points to minutes
        minutes = list(map(convertToMinutes, timePoints))
        
        # Sort the time points
        minutes.sort()
        
        # Initialize the minimum difference as a large number
        min_diff = float('inf')
        
        # Find the minimum difference between consecutive time points
        for i in range(1, len(minutes)):
            min_diff = min(min_diff, minutes[i] - minutes[i - 1])
        
        # Account for the circular nature of the clock (difference between last and first time point)
        min_diff = min(min_diff, 1440 - (minutes[-1] - minutes[0]))
        
        return min_diff
            