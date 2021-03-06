from Figures import King, Queen, Soldier, Tower, Horse, Bishop

class Board:
	"""
    A class used to represent Board in chess game

    Attributes
    ----------
    self.user_white: user attribute, who plays as whites
    self.user_black: user attribute, who plays as blacks
    self.board: main board as nested lists

    Methods
    -------
    figures_placing: placing figures on board function
    board_move_figure: moving the figure function
    check: check function alarming when user's King is under attack
    check_and_mate: check and mate function, deciding who won
    soldier_replace: function replacing soldier when he reachs the first line of the opponent
    """

	def __init__(self, user_white, user_black):
		"""
        Parameters
        ----------
        self.user_white: user attribute, who plays as whites
        self.user_black: user attribute, who plays as blacks

        Attributes
        ----------
		self.board: main board as nested lists
        """

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


	def figures_placing(self):
		"""
	    figures_placing:
		
	    Function, that places figures on board

	    Attributes:
	    ----------
	    self.board: main board of the game
    	"""

		# placing soldiers
		for figure in range(0, 8):
			self.board[6][figure] = Soldier("white")

			self.board[6][figure].position = [6, figure]

			self.board[6][figure].emblem = "♟"

			self.user_white.user_figures.append(self.board[6][figure])

		for figure in range(0, 8):

			self.board[1][figure] = Soldier("black")

			self.board[1][figure].position = [1, figure]

			self.board[1][figure].emblem = "♙"

			self.user_black.user_figures.append(self.board[1][figure])

		# placing Kings
		self.board[0][3], self.board[7][4] = King("black"), King("white")
		self.board[0][3].position, self.board[7][4].position  = [0, 3], [7, 4]
		self.board[0][3].emblem, self.board[7][4].emblem = "♔", "♚"

		self.user_black.user_figures.append(self.board[0][3])
		self.user_white.user_figures.append(self.board[7][4])

		# placing Queens
		self.board[0][4], self.board[7][3] = Queen("black"), Queen("white")
		self.board[0][4].position, self.board[7][3].position  = [0, 4], [7, 3]
		self.board[0][4].emblem, self.board[7][3].emblem = "♕", "♛" 

		self.user_black.user_figures.append(self.board[0][4])
		self.user_white.user_figures.append(self.board[7][3])

		# placing Bishops
		self.board[0][2], self.board[0][5] = Bishop("black"), Bishop("black")
		self.board[7][2], self.board[7][5] = Bishop("white"), Bishop("white")

		self.board[0][2].position, self.board[0][5].position  = [0, 2], [0, 5]
		self.board[7][2].position, self.board[7][5].position  = [7, 2], [7, 5]

		self.board[0][2].emblem, self.board[0][5].emblem = "♗", "♗"
		self.board[7][2].emblem, self.board[7][5].emblem = "♝", "♝"

		self.user_black.user_figures.append(self.board[0][2])
		self.user_white.user_figures.append(self.board[7][2])
		self.user_black.user_figures.append(self.board[0][5])
		self.user_white.user_figures.append(self.board[7][5])

		# placing Horses
		self.board[0][1], self.board[0][6] = Horse("black"), Horse("black")
		self.board[7][1], self.board[7][6] = Horse("white"), Horse("white")

		self.board[0][1].position, self.board[0][6].position  = [0, 1], [0, 6]
		self.board[7][1].position, self.board[7][6].position  = [7, 1], [7, 6]

		self.board[0][1].emblem, self.board[0][6].emblem = "♘", "♘"
		self.board[7][1].emblem, self.board[7][6].emblem = "♞", "♞"

		self.user_black.user_figures.append(self.board[0][1])
		self.user_white.user_figures.append(self.board[7][1])
		self.user_black.user_figures.append(self.board[0][6])
		self.user_white.user_figures.append(self.board[7][6])


		# placing Towers
		self.board[0][0], self.board[0][7] = Tower("black"), Tower("black")
		self.board[7][0], self.board[7][7] = Tower("white"), Tower("white")

		self.board[0][0].position, self.board[0][7].position  = [0, 0], [0, 7]
		self.board[7][0].position, self.board[7][7].position  = [7, 0], [7, 7]

		self.board[0][0].emblem, self.board[0][7].emblem = "♖", "♖"
		self.board[7][0].emblem, self.board[7][7].emblem = "♜", "♜"

		self.user_black.user_figures.append(self.board[0][0])
		self.user_white.user_figures.append(self.board[7][0])
		self.user_black.user_figures.append(self.board[0][7])
		self.user_white.user_figures.append(self.board[7][7])



	def board_move_figure(self, figure_from, figure_to):
		"""
	    board_move_figure:
		
	    Function, that moves figures on board

	    Args:
	    figure_from: from where coordinates
	    figure_to: where to coordinates

	    Attributes:
	    ----------
	    self.figure_object: figure object, that user chose
	    self.figure_object.position: figure object's position
    	"""

		# saving figure_from coordinate object as variable for easy use 
		self.figure_object = self.board[figure_from[0]][figure_from[1]]

		# giving the position for further analysis of avaiable cells for move
		self.figure_object.position = figure_from

		# status variable for status of the True or False condition
		# in case if the possible move is in or out of poss_moves list
		self.status = None

		# direction object to check all the cells in the current figures direction list
		self.direction_check_list = None

		# direction status to know if we need to return False or not
		direction_status = False

		# saving attack direction for further check
		self.attack_direction = None
		
		while True:

			# getting our possible moves for figure
			self.figure_object.gen_possible_moves()

			self.loop_must_break = False

			# checking if the figures coordinates match with possible move cells for figure
			for direction_list in self.figure_object.poss_moves + self.figure_object.poss_attacks:

				self.status = False

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

				if self.loop_must_break:
					break

			self.loop_must_break_2 = False

			for direction_list in self.figure_object.poss_attacks:

				for coordinates in direction_list:

					if figure_to == coordinates:

						self.attack_direction = direction_list

						self.loop_must_break_2 = True

				if self.loop_must_break_2:
					break
	

			# if there is such cell in any direction 
			if self.status:

				# saving move to index for checking all cells before the move to position
				self.move_index = self.direction_check_list.index(figure_to)

				# cells status
				self.cell_status = True

				# second status in case if there is a figure on the final destination
				self.secondary_status = None

				if self.move_index == 0:
					self.move_index = 1
				else:
					pass

				# checking the cells before the last move position
				for cell in range(0, self.move_index):

					main_cell = self.direction_check_list[cell]

					# in case if there is no move further but from_to position, which is not empty
					if self.move_index == 1 and self.board[figure_to[0]][figure_to[1]] != None:

						self.secondary_status = True
						break

					# in case if all cells before the final are empty
					# and the final destination cell is not empty(is another figure object)
					elif self.board[main_cell[0]][main_cell[1]] == None and self.board[figure_to[0]][figure_to[1]] != None:

						self.secondary_status = True
						continue

					# checking if all the cells before the final destination
					# are empty, if so, move goes on
					elif self.board[main_cell[0]][main_cell[1]] == None and self.board[figure_to[0]][figure_to[1]] == None:
						continue

					# this condition is for case, when there is a figure on a way to the last spot
					else:

						self.cell_status = False
						self.secondary_status  = False
						
						break


				# if the loop returns True for cell status
				# and all the way to the last cell is empty
				if self.cell_status and self.secondary_status == None and figure_to in self.direction_check_list:

					# moving the figure
					self.board[figure_to[0]][figure_to[1]] = self.board[figure_from[0]][figure_from[1]]

					# updating position for figure
					self.board[figure_to[0]][figure_to[1]].position = [figure_to[0], figure_to[1]]

					# making previous cell None, as figure started move from there
					# which means it must be empty
					self.board[figure_from[0]][figure_from[1]].update_location()
					self.board[figure_from[0]][figure_from[1]] = None

					# possible moves nullify as we could pack them once more on the next move
					self.board[figure_to[0]][figure_to[1]].positions_cleaning()

				# in case if all the way is empty but there is a figure on the last cell
				elif self.cell_status and self.secondary_status and figure_to in self.attack_direction:

					# checking figure_colors
					# if there is an opponent figure on a way, it's being eaten and the user's figure moves on
					if self.board[figure_to[0]][figure_to[1]].figure_color != self.figure_object.figure_color:

						# as there is an enemy figure on a way, before the moving, we make figure status=False
						# this allows us to delete the figure from users pack and also for other figure movement 
						self.board[figure_to[0]][figure_to[1]].status = False

						# moving the figure
						self.board[figure_to[0]][figure_to[1]] = self.board[figure_from[0]][figure_from[1]]

						# updating position for figure
						self.board[figure_to[0]][figure_to[1]].position = [figure_to[0], figure_to[1]]

						# making previous cell None, as figure started move from there
						# which means it must be empty
						self.board[figure_from[0]][figure_from[1]].update_location()
						self.board[figure_from[0]][figure_from[1]] = None

						# possible moves nullify as we could pack them once more on the next move
						self.board[figure_to[0]][figure_to[1]].positions_cleaning()

					else:
						print("Invalid choice, your figure is on your way")
						direction_status = True
						

				else:
					print("Invalid choice, there is a figure on your way")
					direction_status = True

				break
			# in case if we had False status and there is no such coordinates for figure to move to
			else:
				print("Wrong direction, please enter a valid cell for move")

				direction_status = True
				
				break

		# returning False if there is a need to repeat the move for player
		if direction_status:
			return False
		else:
			pass

	# check function
	def check(self, user):
		"""
	    check:
		
	    check function, that alarms, when user's King is under attack

	    Args:
	    user: user arg to check his King
    	"""

		main_loop = False

		for figure in user.user_figures:

			# generating possible moves
			figure.gen_possible_moves()

			# status to break loop
			loop_break = False

			# cheking the directions if any figure has opponent King under it's attack
			for cells in figure.poss_attacks:

				# cheking every direction 
				for coordinate in cells:

					if self.board[coordinate[0]][coordinate[1]] != None:

						# if there is a king on attack direction
						if type(self.board[coordinate[0]][coordinate[1]]) == King and self.board[coordinate[0]][coordinate[1]].figure_color != figure.figure_color:

							print("It's check!")

							# possible moves and attacks nullify as we could pack them once more on the next move

							figure.positions_cleaning()
							
							loop_break = True
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



	def check_and_mate(self, user_1, user_2):
		"""
	    check_and_mate:
		
	    Check and mate Function that defines who will win

	    Args:
	    user_1: user's arg who's King will be checked
	    user_2: user's arg who's figures which can attack opponents King will be revealed

	    Attributes:
	    ----------
	    self.king_object: User's King object
	    self.figure_object.position: figure object's position
    	"""

		# users' king object 
		self.king_object = None

		# empty list for comparing Kings avaiable moves
		# and opponents cells under attack
		self.opponent_attack_cells = []

		# looking for king
		for king in user_1.user_figures:
			if type(king) == King:
				self.king_object = king
				break
			else:
				continue

		# generating king's possible moves
		self.king_object.gen_possible_moves()

		# saving the list
		self.king_moves = self.king_object.poss_moves

		# kings moves simple coordinates list
		self.king_simple_moves = []

		# checking the directions for king
		for directions in self.king_moves:

			# checking every single direction
			for coordinate in directions:

				if self.board[coordinate[0]][coordinate[1]] != None:

					# checking if the figure is ours or not
					if self.board[coordinate[0]][coordinate[1]].figure_color == self.king_object.figure_color:

						del coordinate

					else:
						continue

		# king move simplify 
		for direction in self.king_moves:
			for coordinate in direction:
				self.king_simple_moves.append(coordinate)

		# checking opponents figure possible attack moves
		for figure in user_2.user_figures:

			figure.gen_possible_moves()

			for direction in figure.poss_attacks:

				for coordinate in direction:

					if coordinate in self.king_simple_moves:

						# so can attack some of king moves
						# saving move to index for checking all cells before the move to position
						self.move_index = direction.index(coordinate)

						# cells status
						self.cell_status = True

						# second status in case if there is a figure on the final destination
						self.secondary_status = None

						# checking the cells before the last move position
						for cell in range(0, self.move_index):

							main_cell = direction[cell]

							# checking if all the cells before the final destination
							# are empty, if so, move goes on
							if self.board[main_cell[0]][main_cell[1]] == None and self.board[coordinate[0]][coordinate[1]] == None:
								continue

							# in case if all cells before the final are empty
							# and the final destination cell is not empty(is another figure object)
							elif self.board[main_cell[0]][main_cell[1]] == None and self.board[coordinate[0]][coordinate[1]] != None:

								self.secondary_status = True
								continue

							# this condition is for case, when there is a figure on a way to the last spot
							else:

								self.cell_status = False
								self.secondary_status  = False
								
								for move in self.king_simple_moves:
									if move == coordinate:
										del move

								break


		if len(self.king_simple_moves) < 1:
			return False
		else:
			return True				


	def soldier_replace(self, user):
		"""
	    soldier_replace:
		
	    Soldier replace Function that replaces soldier as it passes to the opponents first line on board

	    Args:
	    user: user's arg who's soldiers will be checked
    	"""

		trigger = True

		while True:

			# index variable to find the exact figure
			# which has certain position for replacing it
			index = -1

			# color variable to save the color parameter
			# for the further use
			color = None

			# position variable to save the position for the further successeful replacement
			position = None

			# checking every single soldier figure in players figure list
			for figure in user.user_figures:

				# checking the color
				if figure.figure_color == "white":

					# saving the color for the further use
					color = figure.figure_color

					if figure.position[0] == 0 and type(figure) == Soldier:
						position = figure.position
						index += 1
						trigger = False
						break 
					else:
						index += 1


				# checking the color
				elif figure.figure_color == "black":

					# saving the color for the further use
					color = figure.figure_color

					if figure.position[0] == 7 and type(figure) == Soldier:
						position = figure.position
						index += 1
						trigger = False
						break 
					else:
						index += 1

			if trigger:
				break


			sample_figures = ["queen", "bishop", "horse", "tower"]

			print("Which figure do you want?")
			print("Example: bishop")

			user_choice = str(input(": "))

			# loop status
			status = True

			while status:

				if user_choice not in sample_figures:
					print("Please insert correct name of preferable figure")
					user_choice = str(input(": "))

				else:
					status = False


			if user_choice == "queen":
				self.board[position[0]][position[1]] = Queen(color)
				self.board[position[0]][position[1]] = position
				user.user_figures[index] = self.board[position[0]][position[1]]
			elif user_choice == "bishop":
				self.board[position[0]][position[1]] = Bishop(color)
				self.board[position[0]][position[1]] = position
				user.user_figures[index] = self.board[position[0]][position[1]]
			elif user_choice == "horse":
				self.board[position[0]][position[1]] = Horse(color)
				self.board[position[0]][position[1]] = position
				user.user_figures[index] = self.board[position[0]][position[1]]
			elif user_choice == "tower":
				self.board[position[0]][position[1]] = Tower(color)
				self.board[position[0]][position[1]] = position
				user.user_figures[index] = self.board[position[0]][position[1]]

			break
			
	def white_board_print(self):
		"""
	    white_board_print:
		
	   	Function that prints the board

	    Attributes:
	    board_2: board sample for printing
    	"""


		board_2  = [["■", "□", "■", "□", "■", "□", "■", "□"],
					["□", "■", "□", "■", "□", "■", "□", "■"],
					["■", "□", "■", "□", "■", "□", "■", "□"],
					["□", "■", "□", "■", "□", "■", "□", "■"],
					["■", "□", "■", "□", "■", "□", "■", "□"],
					["□", "■", "□", "■", "□", "■", "□", "■"],
					["■", "□", "■", "□", "■", "□", "■", "□"],
					["□", "■", "□", "■", "□", "■", "□", "■"]]


		for i in range(0, 8):
			for b in range(0, 8):
				if self.board[i][b] != None:
					board_2[i][b] = self.board[i][b].emblem

		count = 8

		print()

		for row in board_2:
			print(str(count) + "|" , *row)
			count -= 1

		print("  ", "a", "b", "c", "d", "e", "f", "g", "h")
			
		print()
