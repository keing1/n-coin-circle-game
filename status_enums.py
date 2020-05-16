from enum import Enum

# Enum class denoting possible game statuses - either the user has quit out,
# the game has finished with a winner, or it is a player's turn
class GameStatus(Enum):
    QUIT = 1
    WINNER = 2
    PLAYERTURN = 3

# Enum class denoting whether and how the game should be replayed - either the game
# is replayed with different settings, replayed with new settings, or the game is quit out
class ReplayStatus(Enum):
    SAME = 1
    CHANGE = 2
    QUIT = 3