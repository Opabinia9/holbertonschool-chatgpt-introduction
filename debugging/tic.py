#!/usr/bin/python3
def print_board(board):
    """Display the current board state."""
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board):
    """
    Check if there is a winner on the board.
    
    Parameters:
        board (list): A 3x3 board represented as a list of lists.
    
    Returns:
        bool: True if there is a winner, False otherwise.
    """
    # Check rows
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return True

    # Check columns
    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return True

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return True

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return True

    return False

def is_board_full(board):
    """
    Check if the board is completely filled (draw condition).
    
    Parameters:
        board (list): A 3x3 board represented as a list of lists.
    
    Returns:
        bool: True if the board is full, False otherwise.
    """
    for row in board:
        if " " in row:
            return False
    return True

def get_valid_move(player):
    """
    Get valid row and column input from the player with error handling.
    
    Parameters:
        player (str): The current player ("X" or "O").
    
    Returns:
        tuple: A tuple (row, col) with valid coordinates, or (None, None) if invalid.
    """
    while True:
        try:
            row = int(input(f"Enter row (0, 1, or 2) for player {player}: "))
            col = int(input(f"Enter column (0, 1, or 2) for player {player}: "))
            
            # Validate bounds
            if row < 0 or row > 2 or col < 0 or col > 2:
                print("Error: Row and column must be between 0 and 2. Try again.\n")
                continue
            
            return row, col
        except ValueError:
            print("Error: Invalid input. Please enter numeric values only (0, 1, or 2).\n")
        except KeyboardInterrupt:
            print("\nGame cancelled.")
            return None, None

def tic_tac_toe():
    """Main game loop for Tic Tac Toe."""
    board = [[" "]*3 for _ in range(3)]
    player = "X"
    
    while True:
        print_board(board)
        
        # Get valid move from player
        row, col = get_valid_move(player)
        
        if row is None:
            print("Game ended.")
            return
        
        # Check if spot is already taken
        if board[row][col] != " ":
            print("Error: That spot is already taken! Try again.\n")
            continue
        
        # Place the move
        board[row][col] = player
        
        # Check for winner
        if check_winner(board):
            print_board(board)
            print(f"Player {player} wins!")
            return
        
        # Check for draw
        if is_board_full(board):
            print_board(board)
            print("It's a draw! Game over.")
            return
        
        # Switch player
        player = "O" if player == "X" else "X"

if __name__ == "__main__":
    try:
        tic_tac_toe()
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

