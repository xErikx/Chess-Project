from Figures import King, Queen, Soldier, Tower, Horse, Bishop

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
		for figure in range(0, 8):
			self.board[6][figure] = Soldier("white", True)
			self.board[6][figure].position = [6, figure]

		for figure in range(0, 8):
			self.board[1][figure] = Soldier("black", True)
			self.board[1][figure].position = [1, figure]

		# placing Kings
		self.board[0][3], self.board[7][4] = King("black", "King"), King("white", "King")
		self.board[0][3].position, self.board[7][4].position  = [0, 3], [7, 4]

		# placing Queens
		self.board[0][4], self.board[7][3] = Queen("black", True), Queen("white", True)
		self.board[0][4].position, self.board[7][3].position  = [0, 4], [7, 3]

		# placing Bishops
		self.board[0][2], self.board[0][5] = Bishop("black", True), Bishop("white", True)
		self.board[7][2], self.board[7][5] = Bishop("black", True), Bishop("white", True)
		self.board[0][2].position, self.board[0][5].position  = [0, 2], [0, 5]
		self.board[7][2].position, self.board[7][5].position  = [7, 2], [7, 5]


		# placing Horses
		self.board[0][1], self.board[0][6] = Horse("black", True), Horse("white", True)
		self.board[7][1], self.board[7][6] = Horse("black", True), Horse("white", True)
		self.board[0][1].position, self.board[0][6].position  = [0, 1], [0, 6]
		self.board[7][1].position, self.board[7][6].position  = [7, 1], [7, 6]


		# placing Towers
		self.board[0][0], self.board[0][7] = Tower("black", True), Tower("white", True)
		self.board[7][0], self.board[7][7] = Tower("black", True), Tower("white", True)
		self.board[0][0].position, self.board[0][7].position  = [0, 0], [0, 7]
		self.board[7][0].position, self.board[7][7].position  = [7, 0], [7, 7]


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
					self.board[figure_to[0]][figure_to[1]].poss_moves = [[], [], [], [], [], [], [], []]

					# possible attacks nullify as possible moves with the same logic
					self.board[figure_to[0]][figure_to[1]].poss_attacks = [[], []]

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
						self.board[figure_to[0]][figure_to[1]].poss_moves = [[], [], [], [], [], [], [], []]

						# possible attacks nullify as possible moves with the same logic
						self.board[figure_to[0]][figure_to[1]].poss_attacks = [[], []]

					else:
						print("Invalid choice, your figure is on your way")
				else:
					print("Invalid choice, there is a figure on your way")

				break
			# in case if we had False status and there is no such coordinates for figure to move to
			else:
				print("Wrong direction, please enter a valid cell for move")
				break


	def check(self):

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

					# if there is a king on attack direction
					if self.board[coordinate[0]][coordinate[1]].figure_status == "King" and self.board[coordinate[0]][coordinate[1]].color != figure.color:
						print("It's check!")

						figure.poss_moves = [[], [], [], [], [], [], [], []]

						figure.self.poss_attacks = [[], []]

						loop_break = True

					else:
						continue

				if loop_break:
					main_loop = True
					break

			if main_loop:
				break