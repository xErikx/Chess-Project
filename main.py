import random
from BoardClass import Board
from UserClass import User, UserCommunication, configuration_create
from Figures import King, Queen, Soldier, Tower, Horse, Bishop

TURN = None


# deciding colors for players
def color_decision(first, second):

	color = ["white", "black"]

	choice = random.choice(color)

	if choice == "white":
		print("First as white")
		gameplay(first, second)
	else:
		print("Second as white")
		gameplay(second, first)


def gameplay(user_1, user_2):
	global TURN


	# first user plays as whites
	board = Board(user_1, user_2)
	print(f"{user_1} 1 plays as white and {user_2} as black")
	TURN = True


	# placing the figures for the gameplay
	board.figures_placing()

	while board.check_and_mate(user_1, user_2) and board.check_and_mate(user_2, user_1):

		if TURN == True:
			
			board.white_board_print()
			board.black_board_print()

			print("user_1 turn")
			# board figure move command
			# checking if the direction is correct, else board tries to move with new parameters
			if board.board_move_figure(user_1.user_move_from(), user_1.user_move_to()) != False:

				# checking if the soldier is on the last line of his way and needs replacement
				board.soldier_replace(user_1)

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

			board.black_board_print()
			board.white_board_print()

			print("user_2 turn")
			# board figure move command
			# checking if the direction is correct, else board tries to move with new parameters
			if board.board_move_figure(user_2.user_move_from(), user_2.user_move_to()) != False:

				# checking if the soldier is on the last line of his way and needs replacement
				board.soldier_replace(user_1)

				# checking if there is check for user_1
				board.check(user_2)

				# checking opponents figure statuses
				# if there is a False, then user looses his figure as it was eaten
				user_1.user_figure_check()

				# changing the turn

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

	configuration_create()

	user_1 = User("chess_users.db")
	user_1.connect()	


if __name__ == "__main__":
    main()