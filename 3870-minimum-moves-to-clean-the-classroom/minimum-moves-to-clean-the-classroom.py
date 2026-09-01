from collections import deque

class Solution:
    def minMoves(self, classroom, energy):
        m, n = len(classroom), len(classroom[0])

        litters = {}
        start = None
        idx = 0

        for r in range(m):
            for c in range(n):
                if classroom[r][c] == 'S':
                    start = (r, c)
                elif classroom[r][c] == 'L':
                    litters[(r, c)] = idx
                    idx += 1

        target_mask = (1 << idx) - 1

        sr, sc = start
        start_state = (sr, sc, energy, 0)

        q = deque([(sr, sc, energy, 0, 0)])  # r,c,energy,mask,steps
        visited = {start_state}

        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while q:
            r, c, e, mask, steps = q.popleft()

            if mask == target_mask:
                return steps

            # Cannot move if out of energy and not on reset cell
            if e == 0:
                continue

            for dr, dc in dirs:
                nr, nc = r + dr, c + dc

                if not (0 <= nr < m and 0 <= nc < n):
                    continue

                cell = classroom[nr][nc]

                if cell == 'X':
                    continue

                ne = e - 1
                nmask = mask

                if cell == 'L':
                    nmask |= 1 << litters[(nr, nc)]

                if cell == 'R':
                    ne = energy

                state = (nr, nc, ne, nmask)

                if state not in visited:
                    visited.add(state)
                    q.append((nr, nc, ne, nmask, steps + 1))

        return -1