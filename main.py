import random
import socket
from BoardClass import Board
from UserClass import User, UserCommunication, configuration_create
from Figures import King, Queen, Soldier, Tower, Horse, Bishop

PLAYER1 = None
PLAYER2 = None
TURN = None
SERVER_IP = "127.0.0.1"
PORT = 4040
ADDR = (SERVER_IP, PORT)


# deciding colors for players
def color_decision(first, second):

	color = ["white", "black"]

	choice = random.choice(color)

	if choice == "white":
		gameplay(first, second)
	else:
		gameplay(second, first)


def gameplay(user_1, user_2):
	global TURN
	# first user plays as whites
	board = Board(user_1, user_2)
	print(f"{user_1.nickname} 1 plays as white and {user_2.nickname} as black")
	TURN = True


	# placing the figures for the gameplay
	board.figures_placing()

	while board.check_and_mate(user_1, user_2) and board.check_and_mate(user_2, user_1):

		if TURN == True:
			
			board.white_board_print()
			# board.black_board_print()

			white_move_from = user_1.user_move_from()

			white_move_to = user_1.user_move_to()

			while True:
				if board.board[white_move_from[0]][white_move_from[1]] == None:
					print("Please enter a figure, not an empty cell")

					white_move_from = user_1.user_move_from()

					white_move_to = user_1.user_move_to()

				else:
					break


			# if player chooses wrong color figure
			if board.board[white_move_from[0]][white_move_from[1]].figure_color != "white":
				print("Please choose your figure, you play as whites")
				white_move_from = user_1.user_move_from()

				white_move_to = user_1.user_move_to()
			# board figure move command
			# checking if the direction is correct, else board tries to move with new parameters
			elif board.board_move_figure(white_move_from, white_move_to) != False:

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
				board.board_move_figure(white_move_from, white_move_to)

		else:

			board.white_board_print()
			# board.black_board_print()
			

			black_move_from = user_2.user_move_from()

			black_move_to  = user_2.user_move_to()

			while True:
				if board.board[black_move_from[0]][black_move_from[1]] == None:
					print("Please enter a figure, not an empty cell")

					black_move_from = user_2.user_move_from()

					black_move_to  = user_2.user_move_to()
					
				else:
					break

			if board.board[black_move_from[0]][black_move_from[1]].figure_color != "black":
				print("Please choose your figure, you play as blacks")

				black_move_from = user_2.user_move_from()

				black_move_to  = user_2.user_move_to()

			# board figure move command
			# checking if the direction is correct, else board tries to move with new parameters
			elif board.board_move_figure(black_move_from , black_move_to) != False:

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
				board.board_move_figure(black_move_from , black_move_to)

	# checking who lost and who won
	else:
		if board.check_and_mate(user_1, user_2) == False:
			print(f"It's check and mate \n \
				{user_2.nickname} won!")
			user_2.win_score_update()
			user_1.lose_score_update()
		else:
			print(f"It's check and mate \n \
				{user_2.nickname} won!")
			user_1.win_score_update()
			user_2.lose_score_update()






def main():

	global PLAYER1, PLAYER2
	global SERVER_IP
	global PORT
	global ADDR

	# creating socket
	server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	# binding socket to our address
	server_socket.bind(ADDR)

	# server starts listening
	server_socket.listen()
	print(f"Server is listening on {ADDR}")
	print("Welcome to Chess game!")

	configuration_create()

	# server accepting both players connection
	client_socket, client_addr = server_socket.accept()

	PLAYER1 = User("chess_users.db", client_socket)
	PLAYER1.connect()

	print(f"{PLAYER1.nickname} joined!")

	client_socket, client_addr = server_socket.accept()
	PLAYER2 = User("chess_users.db", client_socket)
	PLAYER2.connect()
	print(f"{PLAYER2.nickname} joined!")

	color_decision(PLAYER1, PLAYER2)

	server_socket.close()




if __name__ == "__main__":
    main()