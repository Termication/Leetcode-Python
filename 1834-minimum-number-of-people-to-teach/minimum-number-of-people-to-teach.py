import collections

class Solution(object):
    def minimumTeachings(self, n, languages, friendships):
        """
        :type n: int
        :type languages: List[List[int]]
        :type friendships: List[List[int]]
        :rtype: int
        """
        # Convert language lists to sets for O(1) lookups
        lang_sets = [set(l) for l in languages]
        
        # Step 1: Identify all users in friendships that cannot communicate
        unconnected_users = set()
        for u, v in friendships:
            # Adjust for 0-indexing
            user_u_idx = u - 1
            user_v_idx = v - 1
            
            # Check for common languages using set intersection
            if not (lang_sets[user_u_idx] & lang_sets[user_v_idx]):
                unconnected_users.add(user_u_idx)
                unconnected_users.add(user_v_idx)
                
        # If everyone can communicate, no teaching is needed
        if not unconnected_users:
            return 0
            
        # Step 2: Find the most common language among the unconnected users
        lang_popularity = collections.defaultdict(int)
        for user_idx in unconnected_users:
            for lang in lang_sets[user_idx]:
                lang_popularity[lang] += 1
                
        # The number of people we can avoid teaching is the count of the most popular language
        max_popularity = 0
        if lang_popularity:
            max_popularity = max(lang_popularity.values())
            
        # Step 3: Calculate the result
        # It's the total number of people needing help minus those who already know the best language
        return len(unconnected_users) - max_popularity
            