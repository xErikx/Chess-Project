from BoardClass import Board




board = Board("User")
board.figures_placing()

board.board_move_figure([7,0], [5,0])


# for item in board.board:
# 	print(item)

print(board.board)