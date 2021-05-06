from figures import King, Queen, Soldier, Tower, Horse, Bishop

class Board:

	def __init__(self, user):

		self.user = user
		self.board = [[None, None, None, None, None, None, None, None],
					  [None, None, None, None, None, None, None, None],
					  [None, None, None, None, None, None, None, None],
					  [None, None, None, None, None, None, None, None],
					  [None, None, None, None, None, None, None, None],
					  [None, None, None, None, None, None, None, None],
					  [None, None, None, None, None, None, None, None],
					  [None, None, None, None, None, None, None, None]]


	# placing the figures on the board function
	def figures_placing(self):
		# placing soldiers
		for figure in self.board[6]:
			figure = Soldier

		for figure in self.board[1]:
			figure = Soldier

		# placing Kings
		Self.board[0][4], self.board[-1][3] = King, King

		# placing Queens
		Self.board[0][4], self.board[-1][3] = Queen, Queen

		# placing Bishops
		Self.board[0][2], self.board[0][-3] = Bishop, Bishop
		Self.board[-1][2], self.board[-1][-3] = Bishop, Bishop

		# placing Horses
		Self.board[0][1], self.board[0][-2] = Horse, Horse
		Self.board[-1][1], self.board[-1][-2] = Horse, Horse

		# placing Towers
		Self.board[0][0], self.board[0][-1] = Tower, Tower
		Self.board[-1][0], self.board[-1][-1] = Tower, Tower

	# giving colors to figures(objects) on board
	def board_initializing(self):
		# initializing blue(black) figures
		for figures in self.board[0]:
			figures = f"\033[1;32;40m {Figures}"
		for figures in self.board[1]:
			figures = f"\033[1;32;40m {Figures}"

		# initializing white figures
		for figures in self.board[7]:
			figures = f"\037[1;32;40m {Figures}"
		for figures in self.board[6]:
			figures = f"\037[1;32;40m {Figures}"



	def board_move_figure(self, self.figure_from, self.figure_to):
		self.figure_from = self.user.user_move_from()
		self.figure_to = self.user.user_move_to()