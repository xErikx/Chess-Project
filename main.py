from BoardClass import Board
from UserClass import User
from Figures import King, Queen, Soldier, Tower, Horse, Bishop








def main():
	
	user_1 = User(None)
	user_2 = User(None)
	board = Board(user_1, user_2)

	board.board[0][3] = King("black")
	user_2.user_figures.append(board.board[0][3])
	board.board[0][3].position = [0, 3]

	board.board[0][0] = Tower("white")
	board.board[0][0].position = [0, 0]
	user_1.user_figures.append(board.board[0][0])

	board.board[7][4] = Tower("white")
	board.board[7][4].position = [7, 4]
	user_1.user_figures.append(board.board[7][4])

	board.board[2][0] = Bishop("white")
	board.board[2][0].position = [2, 0]
	user_1.user_figures.append(board.board[2][0])


	print(board.check_and_mate(user_2, user_1))

	






if __name__ == "__main__":
	main()