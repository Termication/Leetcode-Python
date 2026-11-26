class Solution:
    def canAliceWin(self, n: int) -> bool:
        remove = 10
        alice_turn = True

        while n >= remove:
            n -= remove
            remove -= 1
            alice_turn = not alice_turn

        # If the loop stops on Alice's turn, Alice cannot move -> False.
        # If it stops on Bob's turn, Bob cannot move -> Alice wins (True).
        return not alice_turn