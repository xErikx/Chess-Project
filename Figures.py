

class Figure:

	def __init__(self, figure_color, figure_status=True, emblem=None):
		self.figure_color = figure_color
		# attribute for all possible moves on deck for figure
		self.poss_moves = [[], [], [], [], [], [], [], []]
		# attribute for all possible attack cells for figure on deck
		self.poss_attacks = [[], []]
		# attribute for figures position
		self.position = []
		# attribute for figure status(alive/dead)
		self.figure_status = figure_status
		self.emblem = emblem

		self.original_place = True


	# positions nulify function
	def positions_cleaning(self):

		self.poss_moves = [[], [], [], [], [], [], [], []]

		self.poss_attacks = [[], []]

	def update_location(self):
		self.original_place = False


	
class King(Figure):


	def gen_possible_moves(self):

		
		# forward, backwards, left and right moving
		for count in range(1, 2):

			# checking forward cells
			if self.position[0] - count > -1:
				self.poss_moves[0].append([self.position[0] - count, self.position[1]])

			# cheking backwards cells
			if self.position[0] + count < 8:
				self.poss_moves[1].append([self.position[0] + count, self.position[1]])

			# checking left cells
			if self.position[1] - count > -1:
				self.poss_moves[2].append([self.position[0], self.position[1] - count])

			# checking right cells
			if self.position[1] + count < 8:
				self.poss_moves[3].append([self.position[0], self.position[1] + count])

			# diagonally up right cells
			if self.position[0] - count > -1 and self.position[1] + count < 8:
				self.poss_moves[4].append([self.position[0] - count, self.position[1] + count])

			# diagonally down left cells
			if self.position[0] + count < 8 and self.position[1] - count > -1:
				self.poss_moves[5].append([self.position[0] + count, self.position[1] - count])

			# diagonally up left cells
			if self.position[0] - count > - 1 and self.position[1] - count > -1:
				self.poss_moves[6].append([self.position[0] - count, self.position[1] - count])

			# diagonally down right cells
			if self.position[0] + count < 8 and self.position[1] + count < 8:
				self.poss_moves[7].append([self.position[0] + count, self.position[1] + count])

		# the moves are same as attack spots
		self.poss_attacks = self.poss_moves 


class Queen(Figure):



	def gen_possible_moves(self):

		# forward, backwards, left and right moving
		for count in range(1, 8):
			# checking forward cells
			if self.position[0] - count > -1:
				self.poss_moves[0].append([self.position[0] - count, self.position[1]])
			# cheking backwards cells
			if self.position[0] + count < 8:
				self.poss_moves[1].append([self.position[0] + count, self.position[1]])
			# checking left cells
			if self.position[1] - count > -1:
				self.poss_moves[2].append([self.position[0], self.position[1] - count])
			# checking right cells
			if self.position[1] + count < 8:
				self.poss_moves[3].append([self.position[0], self.position[1] + count])

		# diagonally left/right, up/down moves
		for count in range(1, 8):
			# diagonally up right cells
			if self.position[0] - count > -1 and self.position[1] + count < 8:
				self.poss_moves[4].append([self.position[0] - count, self.position[1] + count])
			# diagonally down left cells
			if self.position[0] + count < 8 and self.position[1] - count > -1:
				self.poss_moves[5].append([self.position[0] + count, self.position[1] - count])
			# diagonally up left cells
			if self.position[0] - count > - 1 and self.position[1] - count > -1:
				self.poss_moves[6].append([self.position[0] - count, self.position[1] - count])
			# diagonally down right cells
			if self.position[0] + count < 8 and self.position[1] + count < 8:
				self.poss_moves[7].append([self.position[0] + count, self.position[1] + count])
			
		# possible moves are the same as possible attacks
		self.poss_attacks = self.poss_moves 


class Soldier(Figure):


	def gen_possible_moves(self):

		# generates moves, where soldier can only move forward if
		# color is white, and backwards if it's black
		move_changer = 1 if self.figure_color == 'white' else -1 

		# initial two steps forward from start
		if self.original_place:
			self.poss_moves[0].append([self.position[0] - 1 * move_changer, self.position[1]])
			self.poss_moves[1].append([self.position[0] - 2 * move_changer, self.position[1]])
		# forward move
		elif 0 < self.position[0] < 7 and  not self.original_place:
			self.poss_moves[2].append([self.position[0] - 1 * move_changer, self.position[1]])

		# possible attack
		# if soldier is on the first column of the board:
		if self.position[1] == 0:
			# diagonal right forward
			self.poss_attacks[0].append([self.position[0] - 1 * move_changer, self.position[1] + 1])
		# if soldier is on the last column of the board
		elif self.position[1] == 7:
			# diagonal left forward
			self.poss_attacks[1].append([self.position[0] - 1 * move_changer, self.position[1] - 1])
		else:
			# diagonal left forward
			self.poss_attacks[0].append([self.position[0] - 1 * move_changer, self.position[1] - 1])
			# diagonal right forward
			self.poss_attacks[1].append([self.position[0] - 1 * move_changer, self.position[1] + 1])



class Tower(Figure):


	def gen_possible_moves(self):

		# forward, backwards, left and right moving
		for count in range(1, 8):
			# checking forward cells
			if self.position[0] - count > -1:
				self.poss_moves[0].append([self.position[0] - count, self.position[1]])
			# cheking backwards cells
			if self.position[0] + count < 8:
				self.poss_moves[1].append([self.position[0] + count, self.position[1]])
			# checking left cells
			if self.position[1] - count > -1:
				self.poss_moves[2].append([self.position[0], self.position[1] - count])
			# checking right cells
			if self.position[1] + count < 8:
				self.poss_moves[3].append([self.position[0], self.position[1] + count])


		self.poss_attacks = self.poss_moves 

	

class Horse(Figure):


	def gen_possible_moves(self):

		if self.position[0] + 2 < 8 and self.position[1] + 1 < 8: #1
			self.poss_moves[0].append([self.position[0] + 2, self.position[1] + 1])

		if self.position[0] + 2 < 8 and self.position[1] - 1 > -1: #2
			self.poss_moves[1].append([self.position[0] + 2, self.position[1] - 1])

		if self.position[0] + 1 < 8 and self.position[1] + 2 < 8: #3
			self.poss_moves[2].append([self.position[0] + 1, self.position[1] + 2])

		if self.position[0] + 1 < 8 and self.position[1] - 2 > -1:
			self.poss_moves[3].append([self.position[0] + 1, self.position[1] - 2])

		if self.position[0] - 2 > -1 and self.position[1] + 1 < 8: #1
			self.poss_moves[4].append([self.position[0] - 2, self.position[1] + 1])

		if self.position[0] - 2 > -1 and self.position[1] - 1 > -1: #2
			# forward left move
			self.poss_moves[5].append([self.position[0] - 2, self.position[1] - 1])

		if self.position[0] - 1 > -1 and self.position[1] + 2 < 8: #3
			self.poss_moves[6].append([self.position[0] - 1, self.position[1] + 2])

		if self.position[0] - 1 > -1 and self.position[1] - 2 > -1:
			self.poss_moves[7].append([self.position[0] - 1, self.position[1] - 2])

		
		# the moves are same as attack spots
		self.poss_attacks = self.poss_moves 


class Bishop(Figure):


	def gen_possible_moves(self):

		# diagonally left/right, up/down moves
		for count in range(1, 8):
			# diagonally up right cells
			if self.position[0] - count > -1 and self.position[1] + count < 8:
				self.poss_moves[1].append([self.position[0] - count, self.position[1] + count])
			# diagonally down left cells
			if self.position[0] + count < 8 and self.position[1] - count > -1:
				self.poss_moves[2].append([self.position[0] + count, self.position[1] - count])
			# diagonally up left cells
			if self.position[0] - count > - 1 and self.position[1] - count > -1:
				self.poss_moves[3].append([self.position[0] - count, self.position[1] - count])
			# diagonally down right cells
			if self.position[0] + count < 8 and self.position[1] + count < 8:
				self.poss_moves[4].append([self.position[0] + count, self.position[1] + count])

		# moves are the same as attacks
		self.poss_attacks = self.poss_moves 