class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        n = len(dominoes)
        time_R = [-1] * n  # Time for rightward force to reach
        time_L = [-1] * n  # Time for leftward force to reach

        # Calculate time for rightward force
        last_R = -1
        for i in range(n):
            if dominoes[i] == 'R':
                last_R = i
                time_R[i] = 0
            elif dominoes[i] == 'L':
                last_R = -1
            elif dominoes[i] == '.' and last_R != -1:
                time_R[i] = i - last_R

        # Calculate time for leftward force
        last_L = -1
        for i in range(n - 1, -1, -1):
            if dominoes[i] == 'L':
                last_L = i
                time_L[i] = 0
            elif dominoes[i] == 'R':
                last_L = -1
            elif dominoes[i] == '.' and last_L != -1:
                time_L[i] = last_L - i

        result = list(dominoes)
        for i in range(n):
            if dominoes[i] == '.':
                r_time = time_R[i]
                l_time = time_L[i]

                if r_time != -1 and l_time != -1:
                    if r_time < l_time:
                        result[i] = 'R'
                    elif r_time > l_time:
                        result[i] = 'L'
                    # If equal, remains '.'
                elif r_time != -1:
                    result[i] = 'R'
                elif l_time != -1:
                    result[i] = 'L'

        return "".join(result)