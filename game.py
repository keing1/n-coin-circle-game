from board import Board
from status_enums import GameStatus, ReplayStatus

class Game:

	def __init__(self):
		self.game_board = None
		self.game_status = None
		self.replay_status = None
		self.num_coins = None
		self.player_1 = None
		self.player_2 = None

	# Run through one or multiple instances of the game
	def run_game(self):
		self.print_rules_str()
		# Session loop
		while self.replay_status is not ReplayStatus.QUIT:
			self.execute_game_start()
			# Game loop
			while self.game_status is GameStatus.PLAYERTURN:
				self.execute_game_turn()

			self.execute_game_end()
		print("Goodbye!")

	# Print string denoting the rules of the game
	def print_rules_str(self):
		print(
			"\nRules: There are n coins (numbered 1 through n, clockwise) in "
			"a circle, each showing either heads or tails. Starting from coin 1, and "
			"proceeding clockwise one coin at a time, players are allowed to flip "
			"the current coin using the following rules: if the current coin is "
			"showing heads, then Player 1 can choose to flip it to tails or to "
			"pass; if the current coin is showing tails, then Player 2 can choose "
			"to flip that coin to heads or to pass. In either case, play then "
			"immediately proceeds to the next coin, and can loop around the circle "
			"as many times as needed. Player 1 wins if all n coins ever end up "
			"facing the same way (all heads or all tails).\n")

	# Execute task of starting the game and initializing variables
	def execute_game_start(self):
		if self.replay_status is not ReplayStatus.SAME:
			num_coins, player_1_name, player_2_name = self.prompt_game_start()
		else:
			num_coins = self.num_coins
			player_1_name = self.player_1
			player_2_name = self.player_2
		self.initialize_game(num_coins, player_1_name, player_2_name)
		self.print_endwarning_str()


	# Prompt user for input on board size as well as player names
	def prompt_game_start(self):
		while True:
			try:
				num_coins = int(input("How many coins should be in the game? "))
			except ValueError:
				print("\nInvalid input - please enter a number.\n")
			if num_coins >= 2:
				break
			else:
				print("\nInvalid input - too few coins.\n")
				continue
		player_1_name = str(input("What is player 1's name? "))
		player_2_name = str(input("What is player 2's name? "))

		return num_coins, player_1_name, player_2_name

	# Given user input, initialize Game instance variables
	def initialize_game(self, num_coins, player_1_name, player_2_name):
		self.game_board = Board(num_coins)
		self.update_game_status(False)
		self.num_coins = num_coins
		self.player_1 = player_1_name
		self.player_2 = player_2_name

	# Print string telling user how to exit out of any game
	def print_endwarning_str(self):
		print("If you ever want to end the game, type [e].")

	# Execute task of going through a particular turn of the game
	def execute_game_turn(self):
		self.game_board.print_board()
		user_input = self.prompt_move()
		quit_bool, flip_bool  = self.process_move_prompt(user_input)
		if not quit_bool:
			self.game_board.update_board(flip_bool)
		self.update_game_status(quit_bool)

	# Prompt user for whether they should flip the coin or pass
	def prompt_move(self):
		curr_coin = self.game_board.board[self.game_board.curr_pos-1]
		while True:
			if curr_coin == "H":
				move = input("{} (p1), would you like to [f]lip from".format(self.player_1) +
					" H to T, or would you like to [p]ass?")
			else:
				move = input("{} (p2), would you like to [f]lip from".format(self.player_2) +
					" T to H, or would you like to [p]ass?")

			if move in ("f", "p", "e"):
				break
			else:
				print("\nThat input was invalid.\n")

		return move

	# Process user move 
	def process_move_prompt(self, user_input):
		assert(user_input in ("e", "f", "p"))

		if user_input == "e":
			quit_bool = True
			flip_bool = None
		elif user_input == "f":
			quit_bool = False
			flip_bool = True
		else:
			quit_bool = False
			flip_bool = False
		
		return quit_bool, flip_bool

	# Update game status, used to determine whether and how to end the game
	def update_game_status(self, quit_bool):
		if quit_bool:
			self.game_status = GameStatus.QUIT
		elif all(elem == self.game_board.board[0] for elem in self.game_board.board):
			self.game_status = GameStatus.WINNER
		else:
			self.game_status = GameStatus.PLAYERTURN

		assert(self.game_status in GameStatus)

	# Execute task of ending the game, including potentially setting game up
	# to be restarted if user desires
	def execute_game_end(self):
		self.game_board.print_board()
		self.print_game_end()
		user_input = self.prompt_replay()
		self.update_replay_status(user_input)

	# Print message to user indicating game has ended
	def print_game_end(self):
		if self.game_status is GameStatus.QUIT:
			print("Game over")
		elif self.game_status is GameStatus.WINNER:
			print("Congratulations, {} wins!".format(self.player_1))
		else:
			print("You should not be here")

	# Prompt user for whether they would like to replay the game
	def prompt_replay(self):
		while True:
			replay_val = input("Would you like to play again with the [s]ame settings," +
				" [c]hange game settings, or [q]uit?")
			if replay_val in ("s", "c", "q"):
				break
			else:
				print("\nThat input was invalid.")
		print("\n")

		return replay_val

	# Update replay status, used for determining whether and how to restart the game
	def update_replay_status(self, user_input):
		assert(user_input in ("s", "c", "q"))
		# Grab the particular replay status enum that corresponds with the input character
		self.replay_status = ReplayStatus._value2member_map_[user_input]


if __name__ == "__main__":
	g = Game()
	g.run_game()