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
		self.board[0][4], self.board[-1][3] = King("black"), King("white")

		# placing Queens
		self.board[0][4], self.board[-1][3] = Queen("black"), Queen("white")

		# placing Bishops
		self.board[0][2], self.board[0][-3] = Bishop(), Bishop()
		self.board[-1][2], self.board[-1][-3] = Bishop(), Bishop()

		# placing Horses
		self.board[0][1], self.board[0][-2] = Horse(), Horse()
		self.board[-1][1], self.board[-1][-2] = Horse(), Horse()

		# placing Towers
		self.board[0][0], self.board[0][-1] = Tower(), Tower()
		self.board[-1][0], self.board[-1][-1] = Tower(), Tower()


	# # giving colors to figures(objects) on board
	# def board_initializing(self):
	# 	# initializing blue(black) figures
	# 	for figures in self.board[0]:
	# 		figures.color = f"\033[1;34;40m {figures}"
	# 	for figures in self.board[1]:
	# 		figures = f"\033[1;34;40m {figures}"

	# 	# initializing white figures
	# 	for figures in self.board[7]:
	# 		figures = f"\033[1;37;40m {Figures}"
	# 	for figures in self.board[6]:
	# 		figures = f"\033[1;37;40m {Figures}"



	def board_move_figure(self, self.figure_from, self.figure_to):
		
		while True:

			# getting our possible moves for figure
			self.board[self.figure_from[0]][self.figure_from[1]].possible_moves

			# checking if the coordinates figure_to match with possible move cells for figure
			for cells in self.board[self.figure_from[0]][self.figure_from[1]].poss_moves:

				# simple move for figure in case if the go to cell is empty 
				if self.board[self.figure_to[0]][self.figure_to[1]] == self.board[cells[0]][cells[1]] and self.board[cells[0]][cells[1]] == None:
					
					# moving the figure to given position 
					self.board[self.figure_to[0]][self.figure_to[1]] = self.board[self.figure_from[0]][self.figure_from[1]]
					
					# making the inital coordinates None as figure moved from there
					self.board[self.figure_from[0]][self.figure_from[1]] = None
					
					# clearing the possible_moves list for figure
					self.board[self.figure_to[0]][self.figure_to[1]].poss_moves = []
					
					# clearing the possible_attacks list for figure
					self.board[self.figure_to[0]][self.figure_to[1]].poss_attacks = []