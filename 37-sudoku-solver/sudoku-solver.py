class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        # Bitmasks for rows, cols, boxes (bit d set means digit d is used)
        rows = [0] * 9
        cols = [0] * 9
        boxes = [0] * 9
        empties = []

        def box_id(r, c):
            return (r // 3) * 3 + (c // 3)

        # Initialize
        for r in range(9):
            for c in range(9):
                ch = board[r][c]
                if ch == '.':
                    empties.append((r, c))
                else:
                    d = ord(ch) - ord('0')  # 1..9
                    bit = 1 << d
                    b = box_id(r, c)
                    rows[r] |= bit
                    cols[c] |= bit
                    boxes[b] |= bit

        FULL = 0x3FE  # bits 1..9

        # popcount replacement for older Python
        def popcount(x):
            cnt = 0
            while x:
                x &= x - 1
                cnt += 1
            return cnt

        # map one-hot bit -> digit
        BIT_TO_DIGIT = {1 << d: d for d in range(1, 10)}

        def dfs():
            if not empties:
                return True

            # MRV: choose cell with fewest candidates
            best_i = -1
            best_mask = 0
            best_cnt = 10
            for i in range(len(empties)):
                r, c = empties[i]
                b = box_id(r, c)
                used = rows[r] | cols[c] | boxes[b]
                cand = (~used) & FULL
                cnt = popcount(cand)
                if cnt == 0:
                    return False
                if cnt < best_cnt:
                    best_cnt = cnt
                    best_i = i
                    best_mask = cand
                    if cnt == 1:
                        break

            r, c = empties.pop(best_i)
            b = box_id(r, c)
            cand = best_mask

            while cand:
                bit = cand & -cand
                d = BIT_TO_DIGIT[bit]

                rows[r] |= bit
                cols[c] |= bit
                boxes[b] |= bit
                board[r][c] = str(d)

                if dfs():
                    return True

                # backtrack
                rows[r] ^= bit
                cols[c] ^= bit
                boxes[b] ^= bit
                board[r][c] = '.'

                cand &= cand - 1  # next candidate

            empties.insert(best_i, (r, c))
            return False

        dfs()