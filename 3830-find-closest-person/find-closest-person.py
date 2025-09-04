class Solution(object):
    def findClosest(self, x, y, z):
        """
        :type x: int
        :type y: int
        :type z: int
        :rtype: int
        """
        # Calculate the absolute distance for each person from person 3
        dist_person1 = abs(x - z)
        dist_person2 = abs(y - z)
        
        # Compare the distances to determine the winner
        if dist_person1 < dist_person2:
            return 1
        elif dist_person2 < dist_person1:
            return 2
        else: # dist_person1 == dist_person2
            return 0