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
		self.board[0][2], self.board[0][-3] = Bishop("black"), Bishop("white")
		self.board[-1][2], self.board[-1][-3] = Bishop("black"), Bishop("white")

		# placing Horses
		self.board[0][1], self.board[0][-2] = Horse("black"), Horse("white")
		self.board[-1][1], self.board[-1][-2] = Horse("black"), Horse("white")

		# placing Towers
		self.board[0][0], self.board[0][-1] = Tower("black"), Tower("white")
		self.board[-1][0], self.board[-1][-1] = Tower("black"), Tower("white")


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

		# saving figure_from coordinate object as variable for easy use 
		self.figure_object = self.board[self.figure_from[0]][self.figure_from[1]]

		# giving the position for further analysis of avaiable cells for move
		self.figure_object.position = self.figure_from

		# status variable for status of the True or False condition
		# in case if the possible move is in or out of poss_moves list
		self.status = None

		# direction object to check all the cells in the current figures direction list
		self.direction_check_list = None

		
		while True:

			# getting our possible moves for figure
			self.figure_object.possible_moves()

			self.loop_must_break = False

			# checking if the coordinates figure_to match with possible move cells for figure
			for direction_list in self.figure_object.poss_moves:

				# looking for exact direction of the move
				for coordinates in direction_list:
					if self.figure_to == coordinates:

						# returning True condition
						self.status = True

						# saving the correct direction for further check of the cells
						self.direction_check_list = direction_list
						
						# stoping the loop
						self.loop_must_break = True
						break
					else:

						# returning False condition in status
						self.status = False

						# stoping the loop
						self.loop_must_break = True
						break
				if self.loop_must_break:
					break

			

			# if there is such cell in any direction 
			if self.status:

				# saving move to index for checking all cells before the move to position
				self.move_index = self.direction_check_list.index(self.figure_to)

				# cells status
				self.cell_status = True

				# checking the cells before the last move position
				for cell in range(self.move_index + 1):

					main_cell = self.direction_check_list[cell]

					if self.board[main_cell[0], main_cell[1]] == None:
						continue

					else:
						self.cell_status = False
						
						break

				if self.cell_status:
					self.board[self.figure_from[0]][self.figure_from[1]] = self.board[self.figure_to[0]][self.figure_to[1]]
					self.board[self.figure_from[0]][self.figure_from[1]] = None
					self.board[self.figure_to[0]][self.figure_to[1]].poss_moves = [[], [], [], [], [], [], ,[], []] 
					self.board[self.figure_to[0]][self.figure_to[1]].poss_attacks = [[], []]
				else:
					print("Invalid choice, there is a figure on your way")

				break
			else:
				print("Wrong direction, please enter a valid cell for move")
				break


