import numpy as np

class Board:

	def __init__(self, num_coins):
		self.num_coins = num_coins
		self.board = self.generate_new_board()
		self.curr_pos = 1
		self.flip_dictionary = {"H": "T", "T": "H"}


	# Generate a random new board with num_coins total coins
	def generate_new_board(self):
		num_heads = np.random.randint(1, self.num_coins)
		num_tails = self.num_coins - num_heads

		my_list = num_heads * ["H"] + num_tails * ["T"]
		np.random.shuffle(my_list)

		return my_list

	# Given a position on the board, this function flips it from heads to tails
	# or vice versa
	def flip_pos(self, pos):
		pos_value = self.board[self.curr_pos - 1]
		self.board[self.curr_pos - 1] = self.flip_dictionary[pos_value]

	# Updates the board given a bool denoting whether the current position should 
	# be flipped
	def update_board(self, flip_bool):
		if flip_bool:
			self.flip_pos(self.curr_pos)

		if self.curr_pos == self.num_coins:
			self.curr_pos = 1
		else:
			self.curr_pos += 1

	# Prints the current board on the command line
	def print_board(self):
		# Create line that will display the board
		separation = 3
		join_str = " " * separation
		board_line = join_str.join(self.board)

		# Create line that will display the position indicator
		pos_indicator_position = (self.curr_pos-1) * (separation+1) + 1
		num_spaces_before = pos_indicator_position - 1
		num_spaces_after = len(board_line) - pos_indicator_position
		indicator_line = " " * num_spaces_before + "^" + " " * num_spaces_after

		print("\nCurrent board:")
		print(board_line)
		print(indicator_line)
		print("\n")