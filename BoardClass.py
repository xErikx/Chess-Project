from Figures import King, Queen, Soldier, Tower, Horse, Bishop

class Board: 

	def __init__(self, user_white, user_black):

		self.user_white = user_white

		self.user_black = user_black

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
		for figure in range(0, 8):
			self.board[6][figure] = Soldier("white")

			self.board[6][figure].position = [6, figure]

			self.user_white.user_figures.append(self.board[6][figure])

		for figure in range(0, 8):

			self.board[1][figure] = Soldier("black")

			self.board[1][figure].position = [1, figure]

			self.user_black.user_figures.append(self.board[1][figure])

		# placing Kings
		self.board[0][3], self.board[7][4] = King("black"), King("white")
		self.board[0][3].position, self.board[7][4].position  = [0, 3], [7, 4]

		self.user_black.user_figures.append(self.board[0][3])
		self.user_white.user_figures.append(self.board[7][4])

		# placing Queens
		self.board[0][4], self.board[7][3] = Queen("black"), Queen("white")
		self.board[0][4].position, self.board[7][3].position  = [0, 4], [7, 3]

		self.user_black.user_figures.append(self.board[0][4])
		self.user_white.user_figures.append(self.board[7][3])

		# placing Bishops
		self.board[0][2], self.board[0][5] = Bishop("black"), Bishop("black")
		self.board[7][2], self.board[7][5] = Bishop("white"), Bishop("white")
		self.board[0][2].position, self.board[0][5].position  = [0, 2], [0, 5]
		self.board[7][2].position, self.board[7][5].position  = [7, 2], [7, 5]

		self.user_black.user_figures.append(self.board[0][2])
		self.user_white.user_figures.append(self.board[7][2])
		self.user_black.user_figures.append(self.board[0][5])
		self.user_white.user_figures.append(self.board[7][5])

		# placing Horses
		self.board[0][1], self.board[0][6] = Horse("black"), Horse("black")
		self.board[7][1], self.board[7][6] = Horse("white"), Horse("white")
		self.board[0][1].position, self.board[0][6].position  = [0, 1], [0, 6]
		self.board[7][1].position, self.board[7][6].position  = [7, 1], [7, 6]

		self.user_black.user_figures.append(self.board[0][1])
		self.user_white.user_figures.append(self.board[7][1])
		self.user_black.user_figures.append(self.board[0][6])
		self.user_white.user_figures.append(self.board[7][6])


		# placing Towers
		self.board[0][0], self.board[0][7] = Tower("black"), Tower("black")
		self.board[7][0], self.board[7][7] = Tower("white"), Tower("white")
		self.board[0][0].position, self.board[0][7].position  = [0, 0], [0, 7]
		self.board[7][0].position, self.board[7][7].position  = [7, 0], [7, 7]

		self.user_black.user_figures.append(self.board[0][0])
		self.user_white.user_figures.append(self.board[7][0])
		self.user_black.user_figures.append(self.board[0][7])
		self.user_white.user_figures.append(self.board[7][7])


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



	def board_move_figure(self, figure_from, figure_to):

		# saving figure_from coordinate object as variable for easy use 
		self.figure_object = self.board[figure_from[0]][figure_from[1]]

		# giving the position for further analysis of avaiable cells for move
		self.figure_object.position = figure_from

		# status variable for status of the True or False condition
		# in case if the possible move is in or out of poss_moves list
		self.status = None

		# direction object to check all the cells in the current figures direction list
		self.direction_check_list = None

		
		while True:

			# getting our possible moves for figure
			self.figure_object.possible_moves()

			self.loop_must_break = False

			# checking if the figures coordinates match with possible move cells for figure
			for direction_list in self.figure_object.poss_moves:

				# looking for exact direction of the move
				for coordinates in direction_list:
					if figure_to == coordinates:

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
				self.move_index = self.direction_check_list.index(figure_to)

				# cells status
				self.cell_status = True

				# second status in case if there is a figure on the final destination
				self.secondary_status = None

				# checking the cells before the last move position
				for cell in range(0, self.move_index):

					main_cell = self.direction_check_list[cell]

					# checking if all the cells before the final destination
					# are empty, if so, move goes on
					if self.board[main_cell[0]][main_cell[1]] == None and self.board[figure_to[0]][figure_to[1]] == None:
						continue

					# in case if all cells before the final are empty
					# and the final destination cell is not empty(is another figure object)
					elif self.board[main_cell[0]][main_cell[1]] == None and self.board[figure_to[0]][figure_to[1]] != None:

						self.secondary_status = True
						continue

					# this condition is for case, when there is a figure on a way to the last spot
					else:

						self.cell_status = False
						self.secondary_status  = False
						
						break

				# if the loop returns True for cell status
				# and all the way to the last cell is empty
				if self.cell_status and self.secondary_status == None:

					# moving the figure
					self.board[figure_to[0]][figure_to[1]] = self.board[figure_from[0]][figure_from[1]]

					# updating position for figure
					self.board[figure_to[0]][figure_to[1]].position = [figure_to[0], figure_to[1]]

					# making previous cell None, as figure started move from there
					# which means it must be empty
					self.board[figure_from[0]][figure_from[1]] = None

					# possible moves nullify as we could pack them once more on the next move
					self.board[figure_to[0]][figure_to[1]].positions_cleaning()

				# 	
				elif self.cell_status and self.secondary_status:

					# checking colors
					# if there is an opponent figure on a way, it's being eaten and the user's figure moves on
					if self.board[figure_to[0]][figure_to[1]].color != self.figure_object.color:

						# as there is an enemy figure on a way, before the moving, we make figure status=False
						# this allows us to delete the figure from users pack and also for other figure movement 
						self.board[figure_to[0]][figure_to[1]].status = False

						# moving the figure
						self.board[figure_to[0]][figure_to[1]] = self.board[figure_from[0]][figure_from[1]]

						# updating position for figure
						self.board[figure_to[0]][figure_to[1]].position = [figure_to[0], figure_to[1]]

						# making previous cell None, as figure started move from there
						# which means it must be empty
						self.board[figure_from[0]][figure_from[1]] = None

						# possible moves nullify as we could pack them once more on the next move
						self.board[figure_to[0]][figure_to[1]].positions_cleaning()

					else:
						print("Invalid choice, your figure is on your way")
				else:
					print("Invalid choice, there is a figure on your way")

				break
			# in case if we had False status and there is no such coordinates for figure to move to
			else:
				print("Wrong direction, please enter a valid cell for move")
				break


	# check function
	def check(self, user):

		main_loop = False

		for figure in user.user_figures:

			# generating possible moves
			figure.possible_moves()

			# status to break loop
			loop_break = False

			# cheking the directions if any figure has opponent King under it's attack
			for cells in figure.poss_attacks:

				# cheking every direction 
				for coordinate in cells:

					if self.board[coordinate[0]][coordinate[1]] != None:

						# if there is a king on attack direction
						if type(self.board[coordinate[0]][coordinate[1]]) == type(King) and self.board[coordinate[0]][coordinate[1]].color != figure.color:

							print("It's check!")

							# possible moves and attacks nullify as we could pack them once more on the next move

							figure.positions_cleaning()

							break

						else:
							break

					else:
						continue

				if loop_break:
					main_loop = True
					break

			if main_loop:
				break


	# check and mate function which defines the win
	def check_and_mate(self, user_1, user_2):

		# users' kign object 
		self.king_object = None

		# empty list for comparing Kings avaiable moves
		# and opponents cells under attack
		self.opponent_attack_cells = []

		# looking for king
		for king in user_1.user_figures:
			if type(king) == type(King):
				self.king_object = king
				break
			else:
				continue

		# generating possible moves for king and saving the list
		self.king_moves = self.king_object.possible_moves()



		# Generating and filling all cells of the opponents figures
		# which can attack King at the moment
		main_loop = False

		for figure in user_2.user_figures:

			# generating possible moves
			figure.possible_moves()

			# status to break loop
			loop_break = False

			# cheking the directions if any figure has opponent King under it's attack
			for cells in figure.poss_attacks:

				# cheking every direction 
				for coordinate in cells:

					if self.board[coordinate[0]][coordinate[1]] != None:

						# if there is a king on attack direction
						if type(self.board[coordinate[0]][coordinate[1]]) == type(King) and self.board[coordinate[0]][coordinate[1]].color != figure.color:

							self.opponent_attack_cells.append(cells)

							# possible moves and attacks nullify as we could pack them once more on the next move

							figure.positions_cleaning()

							break

						else:
							break

					else:
						continue

				if loop_break:
					main_loop = True
					break

			if main_loop:
				break


		self.game_status = False
		
		# comparing cells

		for coordinate in self.king_moves:
			if coordinate in self.opponent_attack_cells:
				continue
			else:
				self.game_status = True
				break

		return self.game_status