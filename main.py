import random
from BoardClass import Board
from UserClass import User
from Figures import King, Queen, Soldier, Tower, Horse, Bishop

TURN = None


# deciding colors for players
def color_decision():

	color = ["white", "black"]

	choice = random.choice(color)

	if choice == "white":
		return True
	else:
		return False


def gameplay(user_1, user_2):
	global TURN

	# deciding colors for players
	color_turn = color_decision()

	# creating a board for gameplay
	if color_turn == True:
		# first user plays as whites
		board = Board(user_1, user_2)
		print(f"{user_1} 1 plays as white and {user_2} as black")
		TURN = True
	else:
		# second user plays as whites
		board = Board(user_2, user_1)
		print(f"{user_2} 2 plays as white and {user_1} as black")
		TURN = False

	# placing the figures for the gameplay
	board.figures_placing()




	while board.check_and_mate(user_1, user_2) and board.check_and_mate(user_2, user_1):

		if TURN == True:

			print("user_1 turn")
			# board figure move command
			# checking if the direction is correct, else board tries to move with new parameters
			if board.board_move_figure(user_1.user_move_from(), user_1.user_move_to()) != False:

				# checking if there is check for user_2
				board.check(user_1)

				# checking opponents figure statuses
				# if there is a False, then user looses his figure as it was eaten
				user_2.user_figure_check()

				# changing the turn

				TURN = False

			# in case if the move was wrong, we give another chance for player
			else:
				board.board_move_figure(user_1.user_move_from(), user_1.user_move_to())

		else:

			print("user_2 turn")
			# board figure move command
			# checking if the direction is correct, else board tries to move with new parameters
			if board.board_move_figure(user_2.user_move_from(), user_2.user_move_to()) != False:

				# checking if there is check for user_1
				board.check(user_2)

				# checking opponents figure statuses
				# if there is a False, then user looses his figure as it was eaten
				user_1.user_figure_check()

				# changing the turn
				print("Black Turn")
				TURN = True

			# in case if the move was wrong, we give another chance for player
			else:
				board.board_move_figure(user_2.user_move_from(), user_2.user_move_to())

	# checking who lost and who won
	else:
		if board.check_and_mate(user_1, user_2) == False:
			print(f"It's check and mate \n \
				{user_2.nickname} won!")
			user_2.win_score += 1
			user_1.lose_score += 1
		else:
			print(f"It's check and mate \n \
				{user_2.nickname} won!")
			user_1.win_score += 1
			user_2.lose_score += 1






def main():
	
	user_1 = User(None)
	user_2 = User(None)
	gameplay(user_1, user_2)
	

if __name__ == "__main__":
    main()