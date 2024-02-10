board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

while True:
    player1 = int(input("Player 1, enter your 'x' (1-9): "))
    for row in range(3):
        for col in range(3):
            if board[row][col] == player1:
                board[row][col] = 'X'
    for row in board:
        print(row)
    if (board[0][0] == board[0][1] == board[0][2] == 'X' or
        board[1][0] == board[1][1] == board[1][2] == 'X' or
        board[2][0] == board[2][1] == board[2][2] == 'X' or
        board[0][0] == board[1][0] == board[2][0] == 'X' or
        board[0][1] == board[1][1] == board[2][1] == 'X' or
        board[0][2] == board[1][2] == board[2][2] == 'X' or
        board[0][0] == board[1][1] == board[2][2] == 'X' or
        board[0][2] == board[1][1] == board[2][0] == 'X'):
        print("Player 1 wins!")
        break
    if all(isinstance(cell, str) for row in board for cell in row):
        print("It's a tie!")
        break
    player2 = int(input("Player 2, enter your move (1-9): "))
    for row in range(3):
        for col in range(3):
            if board[row][col] == player2:
                board[row][col] = 'O'
    for row in board:
        print(row)
    if (board[0][0] == board[0][1] == board[0][2] == 'O' or
        board[1][0] == board[1][1] == board[1][2] == 'O' or
        board[2][0] == board[2][1] == board[2][2] == 'O' or
        board[0][0] == board[1][0] == board[2][0] == 'O' or
        board[0][1] == board[1][1] == board[2][1] == 'O' or
        board[0][2] == board[1][2] == board[2][2] == 'O' or
        board[0][0] == board[1][1] == board[2][2] == 'O' or
        board[0][2] == board[1][1] == board[2][0] == 'O'):
        print("Player 2 wins!")
        break