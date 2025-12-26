class Solution(object):
    def bestClosingTime(self, customers):
        """
        :type customers: str
        :rtype: int
        """
        n = len(customers)
        totalY = customers.count('Y')
        
        prefixN = [0] * (n+1)
        prefixY = [0] * (n+1)
        
        for i in range(1, n+1):
            prefixN[i] = prefixN[i-1] + (1 if customers[i-1] == 'N' else 0)
            prefixY[i] = prefixY[i-1] + (1 if customers[i-1] == 'Y' else 0)
        
        minPenalty = float('inf')
        bestHour = 0
        
        for j in range(n+1):
            penalty = prefixN[j] + (totalY - prefixY[j])
            if penalty < minPenalty:
                minPenalty = penalty
                bestHour = j
        
        return bestHour
