# Descrição: Criação de uma matriz 8x8 com valores 0
EMPTY = 0
board = []

for i in range(8):
    row = [EMPTY for j in range(8)]
    board.append(row)

print(board)

# Descrição: Criação de uma matriz 8x8 com valores 0
board = [[EMPTY for i in range(8)] for j in range(8)]

ROOK = '♖'
KNIGHT = '♘'
PAWN = '♙'
board[0][0] = ROOK
board[0][7] = ROOK
board[7][0] = ROOK
board[7][7] = ROOK
board[4][2] = KNIGHT
board[3][4] = PAWN

for linha in board:
    print(linha)
