# Coin game strategy

I first learned of this game on a math puzzle Facebook group from Nicolas Schank. Accompanying a description of the game, he asked whether Player 1 had a winning strategy. It turns out that Player 1 has a winning strategy in all starting positions. Below I've written out a strategy I came up with along with a proof that it guarantees a win.

## Strategy description
Let's say the longest chain of heads on the board is of length m. We can orient the board such that the last head in the chain is at position n in the circle, and the first head in the chain is at position n-m+1 of the circle.

The strategy for player 1 is described as follows:

1. Pass on every heads until you get to position 1 of the circle.
2. Once you get to position 1 of the circle, flip every heads you see to tails until player 2 flips some coin from tails to heads. Once player 2 does this, then go back to step 1.

Below I've written two examples of what could happen in step 2 to make clear what it is saying:

1. If player 2 doesn't flip any coins from tails to heads, then you will just flip all heads to tails and win.
2. If player 2 flips a coin from tails to heads before you come across any heads, then you won't flip any coins until you get back to position 1.

If you follow this strategy, either player 2 will be forced to let you flip all coins from heads to tails, or player 2 will have to fill the entire board with heads. Either way, player 1 ends up winning.

## Proof of strategy
### Outline of proof
We define a metric called "closeness" on positions of the board. Following the above strategy will result in a position's closeness to increase every time you get back to position 1 of the circle. Since there are a finite number of possible positions on the board, and the maximum closeness positions are when there are long chains of heads, we will eventually fill up the board with heads.

### Details of proof
I define a metric called closeness which is designed to measure how close coins showing heads are to position n, clockwise.
Given a board position A, we define its closeness as follows:
Let's say position A has m heads, which are at indices ![p_1, p_2, ..., p_m](https://render.githubusercontent.com/render/math?math=p_1%2C%20p_2%2C%20...%2C%20p_m) on the circle, such that ![p_1 > p_2 > ... > p_m](https://render.githubusercontent.com/render/math?math=p_1%20%3E%20p_2%20%3E%20...%20%3E%20p_m).
We define closeness as follows: 

![closeness(A) = \sum_{i=1}^m (n+1)^{n-i} p_i](https://render.githubusercontent.com/render/math?math=closeness(A)%20%3D%20%5Csum_%7Bi%3D1%7D%5Em%20(n%2B1)%5E%7Bn-i%7D%20p_i)

All the above formula is saying is that when comparing the closeness of two positions A, and B, A has higher closeness if A has heads at higher indices than B does, where you first compare the indices of the highest index heads, then the second highest index heads, then the third index heads, and so on.

When following the above strategy, every time the board goes through a full "round" starting from position 1 and going back to position 1, the board's closeness must increase. There are two possibilities. One possibility is that player 2 flips tails to heads before player 1 flips any heads to tails. In this case the board's closeness increases because adding additional heads increases a board's closeness. The other possibility is that player 1 starts flipping heads to tails. If player 2 doesn't flip any coins from tails to heads, then player 1 will flip everything to tails and win. So player 2  must eventually flip some coins from tails to heads. This means that there will be heads with higher indices than there were and the board's closeness will increase.

The board's closeness increases every round. Since there are a finite number of positions on the board, we must eventually get to the position of maximum closeness, where all coins are heads. At this point, all coins are the same, so player 1 wins.