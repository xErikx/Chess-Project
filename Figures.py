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
		# diagonal right forward
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
		# forward move
		self.poss_moves.append([self.position[0] - 1, self.position[1]])

	def possible_soldier_attacks(self):
		# diagonal left forward
		self.poss_attacks.append([self.position[0] - 1, self.position[1] - 1])
		# diagonal right forward
		self.poss_attacks.append([self.position[0] - 1, self.position[1] + 1])


class Tower(Figure):

	def __init__(self, figure_color):

		self.figure_color = figure_color

	def possible_tower_moves(self):
		self.counter = 1

		while -1 < self.position[0] < 8 and -1 < self.position[1] < 8:
			# forward move
			self.poss_moves.append([self.position[0] - self.counter, self.position[1]])
			# backwards move
			self.poss_moves.append([self.position[0] + self.counter, self.position[1]])
			# right move
			self.poss_moves.append([self.position[0], self.position[1] + self.counter])
			# left move
			self.poss_moves.append([self.position[0], self.position[1] - self.counter])
			self.counter += 1

		self.counter = 1
		self.poss_moves = self.poss_attacks

	

class Horse(Figure):

	def __init__(self, figure_color):

		self.figure_color = figure_color

	def possible_horse_moves(self):

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