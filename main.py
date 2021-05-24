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
		board = Board(user_1, user_2)
		TURN = True
	else:
		board = Board(user_2, user_1)
		TURN = False

	# placing the figures for the gameplay
	board.figures_placing()


	while board.check_and_mate(user_1, user_2) and board.check_and_mate(user_2, user_1):

		if TURN == True:
			# board figure move command
			board.board_move_figure(user_1.user_move_from(), user_1.user_move_to())

			# checking if the direction is correct, else board tries to move with new parameters
			if board.board_move_figure(user_1.user_move_from(), user_1.user_move_to()) != False:

				# checking if there is check for user_2
				board.check(user_1)

				# checking opponents figure statuses
				# if there is a False, then user looses his figure as it was eaten
				user_2.user_figure_check()

				# changing the turn
				Turn = False

			# in case if the move was wrong, we give another chance for player
			else:
				board.board_move_figure(user_1.user_move_from(), user_1.user_move_to())
		else:
			# board figure move command
			board.board_move_figure(user_2.user_move_from(), user_2.user_move_to())

			# checking if the direction is correct, else board tries to move with new parameters
			if board.board_move_figure(user_2.user_move_from(), user_2.user_move_to()) != False:

				# checking if there is check for user_1
				board.check(user_2)

				# checking opponents figure statuses
				# if there is a False, then user looses his figure as it was eaten
				user_1.user_figure_check()

				# changing the turn
				Turn = True

			# in case if the move was wrong, we give another chance for player
			else:
				board.board_move_figure(user_2.user_move_from(), user_2.user_move_to())

	# checking who lost and who won
	else:
		if board.check_and_mate(user_1, user_2) == False:
			print(f"{user_2.name} won!")
			user_2.win_score += 1
			user_1.lose_score += 1
		else:
			print(f"{user_1.name} won!")
			user_1.win_score += 1
			user_2.lose_score += 1






def main():
	
	user_1 = User(None)
	user_2 = User(None)
	

if __name__ == "__main__":
    main()