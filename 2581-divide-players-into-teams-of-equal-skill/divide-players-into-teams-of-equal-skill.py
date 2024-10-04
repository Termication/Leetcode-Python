class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()  # Sort the array of player skills
        n = len(skill)
        
        # Determine the total skill sum for each team by adding the first and last element
        total_skill = skill[0] + skill[-1]
        
        chemistry_sum = 0
        
        for i in range(n // 2):
            # Check if the sum of the smallest and largest remaining elements is equal to the first team sum
            if skill[i] + skill[n - 1 - i] != total_skill:
                return -1
            
            # Calculate the chemistry for this team
            chemistry_sum += skill[i] * skill[n - 1 - i]
        
        return chemistry_sum
            