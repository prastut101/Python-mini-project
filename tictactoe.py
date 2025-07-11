myDict = {
    "O": "Zero",
    "X": "Cross"
}

# Convert board positions to pretty visuals
def print_board(board):
    print()
    for i in range(3):
        row = []
        for j in range(3):
            val = board[i][j]
            cell = val if val else str(i * 3 + j + 1)
            row.append(cell)
        print(" " + " | ".join(row))
        if i < 2:
            print("---|---|---")
    print()

# Check if player has won
def check_winner(player, board):
    for row in board:
        if row[0] == row[1] == row[2] == player:
            print(f"🎉 {myDict[player]} wins via row!")
            return True
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] == player:
            print(f"🎉 {myDict[player]} wins via column!")
            return True
    if board[0][0] == board[1][1] == board[2][2] == player:
        print(f"🎉 {myDict[player]} wins via diagonal!")
        return True
    if board[0][2] == board[1][1] == board[2][0] == player:
        print(f"🎉 {myDict[player]} wins via diagonal!")
        return True
    return False

# Check if it's a draw
def is_draw(board):
    for row in board:
        if None in row:
            return False
    return True

# Main game
def play_game():
    board = [[None, None, None] for _ in range(3)]
    current_player = "X"

    print("🎮 Welcome to Classic Tic Tac Toe!")
    print("👉 Choose a position (1-9) to place your mark.")
    print_board(board)

    while True:
        try:
            print(f"{myDict[current_player]}'s turn ({current_player})")
            pos = int(input("Enter position (1-9): "))

            if pos < 1 or pos > 9:
                print("⚠️ Please choose a number between 1 and 9.")
                continue

            row = (pos - 1) // 3
            col = (pos - 1) % 3

            if board[row][col] is not None:
                print("⛔ That spot is already taken. Try another.")
                continue

            board[row][col] = current_player
            print_board(board)

            if check_winner(current_player, board):
                break

            if is_draw(board):
                print("🤝 It's a draw! Nobody wins.")
                break

            current_player = "O" if current_player == "X" else "X"

        except ValueError:
            print("⚠️ Invalid input. Enter a number from 1 to 9.")
        except Exception as e:
            print(f"🔥 Unexpected error: {e}")

# Run it
play_game()
