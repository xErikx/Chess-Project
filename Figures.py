class Figure:

	def __init__(self, board):

		self.board = board
		# attribute for all possible moves on deck for figure
		self.poss_moves = [] 
		# attribute for all possible attack cells for figure on deck
		self.poss_attacks = []
		# attribute for figures position
		self.position = []
	
	
class King(Figure):

	def __init__(self, figure_color):
		self.figure_color = figure_color

	def possible_King_moves(self):

		# if king is on left down corner
		if self.postion[0] == 7 and self.position[1] == 0:
			# forward move
			self.poss_moves.append([self.position[0] - 1, self.position[1]])
			# move to right
			self.poss_moves.append([self.position[0], self.position[1] + 1])
			# diagonal right forward
			self.poss_moves.append([self.position[0] - 1, self.position[1] + 1])

		# if king is on the right down corner
		elif self.postion[0] == 7 and self.position[1] == 7:
			# forward move
			self.poss_moves.append([self.position[0] - 1, self.position[1]])
			# move to left
			self.poss_moves.append([self.position[0], self.position[1] - 1])
			# diagonal left forward
			self.poss_moves.append([self.position[0] - 1, self.position[1] - 1])

		# if king is on the top left corner
		elif self.postion[0] == 0 and self.position[1] == 0:
			# backwards move
			self.poss_moves.append([self.position[0] + 1, self.position[1]])
			# move to right
			self.poss_moves.append([self.position[0], self.position[1] + 1])
			# diagonal right backwards
			self.poss_moves.append([self.position[0] + 1, self.position[1] + 1])

		# if king is on the top right corner
		elif self.postion[0] == 0 and self.position[1] == 7:
			# backwards move
			self.poss_moves.append([self.position[0] + 1, self.position[1]])
			# move to left
			self.poss_moves.append([self.position[0], self.position[1] - 1])
			# diagonal left backwards
			self.poss_moves.append([self.position[0] + 1, self.position[1] - 1])

		else:
			# if king is on first line of the board
			if self.postion[0] == 7:
				# forward move
				self.poss_moves.append([self.position[0] - 1, self.position[1]])
				# move to left
				self.poss_moves.append([self.position[0], self.position[1] - 1])
				# move to right
				self.poss_moves.append([self.position[0], self.position[1] + 1])
				# diagonal left forward
				self.poss_moves.append([self.position[0] - 1, self.position[1] - 1])
				# diagonal right forward
				self.poss_moves.append([self.position[0] - 1, self.position[1] + 1])
			# if king is on the last line of the board
			elif self.position[0] == 0:
				# backwards move
				self.poss_moves.append([self.position[0] + 1, self.position[1]])
				# move to left
				self.poss_moves.append([self.position[0], self.position[1] - 1])
				# move to right
				self.poss_moves.append([self.position[0], self.position[1] + 1])
				# diagonal left backwards
				self.poss_moves.append([self.position[0] + 1, self.position[1] - 1])
				# diagonal right backwards
				self.poss_moves.append([self.position[0] + 1, self.position[1] + 1])
			# if king is on the first column of the board
			elif self.position[1] == 0:
				# forward move
				self.poss_moves.append([self.position[0] - 1, self.position[1]])
				# backwards move
				self.poss_moves.append([self.position[0] + 1, self.position[1]])
				# move to right
				self.poss_moves.append([self.position[0], self.position[1] + 1])
				# diagonal right forward
				self.poss_moves.append([self.position[0] - 1, self.position[1] + 1])
				# diagonal right backwards
				self.poss_moves.append([self.position[0] + 1, self.position[1] + 1])
			# if king is on the last column of the board
			elif self.position[1] == 7:
				# forward move
				self.poss_moves.append([self.position[0] - 1, self.position[1]])
				# backwards move
				self.poss_moves.append([self.position[0] + 1, self.position[1]])
				# move to left
				self.poss_moves.append([self.position[0], self.position[1] - 1])
				# diagonal left forward
				self.poss_moves.append([self.position[0] - 1, self.position[1] - 1])
				# diagonal left backwards
				self.poss_moves.append([self.position[0] + 1, self.position[1] - 1])
			else:
				# forward move
				self.poss_moves.append([self.position[0] - 1, self.position[1]])
				# backwards move
				self.poss_moves.append([self.position[0] + 1, self.position[1]])
				# move to left
				self.poss_moves.append([self.position[0], self.position[1] - 1])
				# move to right
				self.poss_moves.append([self.position[0], self.position[1] + 1])
				# diagonal left forward
				self.poss_moves.append([self.position[0] - 1, self.position[1] - 1])
				# diagonal right forward
				self.poss_moves.append([self.position[0] - 1, self.position[1] + 1])
				# diagonal left backwards
				self.poss_moves.append([self.position[0] + 1, self.position[1] - 1])
				# diagonal right backwards
				self.poss_moves.append([self.position[0] + 1, self.position[1] + 1])

		# the moves are same as attack spots
		self.poss_moves = self.poss_attacks


class Queen(Figure):

	def __init__(self, figure_color):

		self.figure_color = figure_color

	def possible_queen_moves(self):
		counter = 1

		while -1 < self.position[0] < 8 and -1 < self.position[1] < 8:
			# forward move
			self.poss_moves.append([self.position[0] - self.counter, self.position[1]])
			# backwards move
			self.poss_moves.append([self.position[0] + self.counter, self.position[1]])
			# right move
			self.poss_moves.append([self.position[0], self.position[1] + self.counter])
			# left move
			self.poss_moves.append([self.position[0], self.position[1] - self.counter])
			# diagonal left forward
			self.poss_moves.append([self.position[0] - self.counter, self.position[1] - self.counter])
			# diagonal right forward
			self.poss_moves.append([self.position[0] - self.counter, self.position[1] + self.counter])
			# diagonal left backwards
			self.poss_moves.append([self.position[0] + self.counter, self.position[1] - self.counter])
			# diagonal right backwards
			self.poss_moves.append([self.position[0] + self.counter, self.position[1] + self.counter])
			self.counter += 1

		self.counter = 1
		self.poss_moves = self.poss_attacks

class Soldier(Figure):

	def __init__(self, figure_color):

		self.figure_color = figure_color

	def possible_soldier_moves(self):
		# initial two steps forward from start
		if self.position[0] == 6:
			self.poss_moves.append([self.position[0] - 1, self.position[1]])
			self.poss_moves.append([self.position[0] - 2, self.position[1]])
		# forward move
		elif self.position[0] < 7 and self.position[0] != 6:
			self.poss_moves.append([self.position[0] - 1, self.position[1]])

	def possible_soldier_attacks(self):

		# if soldier is on the first column of the board:
		if self.position[1] = 0:
			# diagonal right forward
			self.poss_attacks.append([self.position[0] - 1, self.position[1] + 1])
		# if soldier is on the last column of the board
		elif self.position[1] = 7:
			# diagonal left forward
			self.poss_attacks.append([self.position[0] - 1, self.position[1] - 1])
		else:
			# diagonal left forward
			self.poss_attacks.append([self.position[0] - 1, self.position[1] - 1])
			# diagonal right forward
			self.poss_attacks.append([self.position[0] - 1, self.position[1] + 1])


class Tower(Figure):

	def __init__(self, figure_color):

		self.figure_color = figure_color

	def possible_tower_moves(self):

		# if tower is in the left down corner
		if self.position[0] == 7 and self.position[1] == 0:
			# forward move
			for count in range(1, 0 + self.position[0] + 1):
				self.poss_moves.append([self.position[0] - count, self.position[1]])
			# right move
			for count in range(1, 8 - self.position[1]):
				self.poss_moves.append([self.position[0], self.position[1] + count])
		# if tower is in the right down corner
		elif self.position[0] == 7 and self.position[1] == 7:
			# forward move
			for count in range(1, self.position[0] + 1):
				self.poss_moves.append([self.position[0] - count, self.position[1]])
			# left move
			for count in range(1, self.position[1] + 1):
				self.poss_moves.append([self.position[0], self.position[1] - count])
		# if tower is in the left top corner
		elif self.position[0] == 0 and self.position[1] == 0:
			# backwards move
			for count in range(1, 8 - self.position[0]):
				self.poss_moves.append([self.position[0] + count, self.position[1]])
			# right move
			for count in range(1, 8 - self.position[1]):
				self.poss_moves.append([self.position[0], self.position[1] + count])
		# if tower is in the right top corner
		elif self.position[0] == 0 and self.position[1] == 7:
			# backwards move
			for count in range(1, 8 - self.position[0]):
				self.poss_moves.append([self.position[0] + count, self.position[1]])
			# left move
			for count in range(1, self.position[1] + 1)
				self.poss_moves.append([self.position[0], self.position[1] - count])
		# if tower is in the first column on the board
		elif 0 < self.position[0] < 7 and self.position[1] == 0:
			# right move
			for count in range(1, 8 - self.position[1]):
				self.poss_moves.append([self.position[0], self.position[1] + count])
			# forward move
			for count in range(1, self.position[0] + 1):
				self.poss_moves.append([self.position[0] - count, self.position[1]])
			# backwards move
			for count in range(1, 8 - self.position[0]):
				self.poss_moves.append([self.position[0] + count, self.position[1]])
		# if tower is in the last column on the board
		elif 0 < self.position[0] < 7 and self.position[1] == 7:
			# forward move
			for count in range(1, self.position[0] + 1):
				self.poss_moves.append([self.position[0] - count, self.position[1]])
			# backwards move
			for count in range(1, 8 - self.position[0]):
				self.poss_moves.append([self.position[0] + count, self.position[1]])
			# left move
			for count in range(1, self.position[1] + 1)
				self.poss_moves.append([self.position[0], self.position[1] - count])
		# if the tower is in the first line of the board
		elif self.position[0] == 7 and 0 < self.position[1] < 7:
			# forward move
			for count in range(1, self.position[0] + 1):
				self.poss_moves.append([self.position[0] - count, self.position[1]])
			# left move
			for count in range(1, self.position[1] + 1)
				self.poss_moves.append([self.position[0], self.position[1] - count])
			# right move
			for count in range(1, 8 - self.position[1]):
				self.poss_moves.append([self.position[0], self.position[1] + count])
		# if the tower is in the last line(top line) of the board
		elif self.position[0] == 0 and 0 < self.position[1] < 7:
			# backwards move
			for count in range(1, 8 - self.position[0]):
				self.poss_moves.append([self.position[0] + count, self.position[1]])
			# left move
			for count in range(1, self.position[1] + 1)
				self.poss_moves.append([self.position[0], self.position[1] - count])
			# right move
			for count in range(1, 8 - self.position[1]):
				self.poss_moves.append([self.position[0], self.position[1] + count])
		else:
			# forward move
			for count in range(1, self.position[0] + 1):
				self.poss_moves.append([self.position[0] - count, self.position[1]])
			# backwards move
			for count in range(1, 8 - self.position[0]):
				self.poss_moves.append([self.position[0] + count, self.position[1]])
			# left move
			for count in range(1, self.position[1] + 1)
				self.poss_moves.append([self.position[0], self.position[1] - count])
			# right move
			for count in range(1, 8 - self.position[1]):
				self.poss_moves.append([self.position[0], self.position[1] + count])


		self.poss_moves = self.poss_attacks

	

class Horse(Figure):

	def __init__(self, figure_color):

		self.figure_color = figure_color

	def possible_horse_moves(self):
		# if horse is on the left down corner
		if self.position[0] == 7 and self.position[1] == 0:
			# forward right move
			self.poss_moves.append([self.position[0] - 2, self.position[1] + 1])
			# right forward move
			self.poss_moves.append([self.position[0] - 1, self.position[1] + 2])
		# if horse is on the right down corner
		elif self.position[0] == 7 and self.position[1] == 7:
			# forward left move
			self.poss_moves.append([self.position[0] - 2, self.position[1] - 1])
			# left forward move
			self.poss_moves.append([self.position[0] - 1, self.position[1] - 2])
		# if horse is on the left upper corner
		elif self.position[0] == 0 and self.position[1] == 0:
			# bakcwards right move
			self.poss_moves.append([self.position[0] + 2, self.position[1] + 1])
			# right backwards move
			self.poss_moves.append([self.position[0] + 1, self.position[1] + 2])
		# if horse is on the right upper corner
		elif self.position[0] == 0 and self.position[1] == 7:
			# backwards left move
			self.poss_moves.append([self.position[0] + 2, self.position[1] - 1])
			# left backwards move
			self.poss_moves.append([self.position[0] + 1, self.position[1] - 2])
		# if horse is on the first line of the board
		elif self.position[0] == 7:
			if 1 < self.position[1] < 6:
				# forward left move
				self.poss_moves.append([self.position[0] - 2, self.position[1] - 1])
				# forward right move
				self.poss_moves.append([self.position[0] - 2, self.position[1] + 1])
				# left forward move
				self.poss_moves.append([self.position[0] - 1, self.position[1] - 2])
				# right forward move
				self.poss_moves.append([self.position[0] - 1, self.position[1] + 2])
			else:
				# forward left move
				self.poss_moves.append([self.position[0] - 2, self.position[1] - 1])
				# forward right move
				self.poss_moves.append([self.position[0] - 2, self.position[1] + 1])




		# forward left move
		self.poss_moves.append([self.position[0] - 2, self.position[1] - 1])
		# forward right move
		self.poss_moves.append([self.position[0] - 2, self.position[1] + 1])
		# backwards left move
		self.poss_moves.append([self.position[0] + 2, self.position[1] - 1])
		# bakcwards right move
		self.poss_moves.append([self.position[0] + 2, self.position[1] + 1])
		# left forward move
		self.poss_moves.append([self.position[0] - 1, self.position[1] - 2])
		# right forward move
		self.poss_moves.append([self.position[0] - 1, self.position[1] + 2])
		# left backwards move
		self.poss_moves.append([self.position[0] + 1, self.position[1] - 2])
		# right backwards move
		self.poss_moves.append([self.position[0] + 1, self.position[1] + 2])
		# the moves are same as attack spots
		self.poss_moves = self.poss_attacks

class Bishop(Figure):

	def __init__(self, figure_color):

		self.figure_color = figure_color

	def possible_bishop_moves(self):

		self.counter = 1

		while -1 < self.position[0] < 8 and -1 < self.position[1] < 8:

			# diagonal left forward
			self.poss_moves.append([self.position[0] - self.counter, self.position[1] - self.counter])
			# diagonal right forward
			self.poss_moves.append([self.position[0] - self.counter, self.position[1] + self.counter])
			# diagonal left backwards
			self.poss_moves.append([self.position[0] + self.counter, self.position[1] - self.counter])
			# diagonal right backwards
			self.poss_moves.append([self.position[0] + self.counter, self.position[1] + self.counter])
			self.counter += 1

		self.counter = 1
		self.poss_moves = self.poss_attacks