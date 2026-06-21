def is_safe(board, row, col, N):
    for i in range(row):
        if board[i][col] == 1:
            return False
    i = row
    j = col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1
    i = row
    j = col
    while i >= 0 and j < N:
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1
    return True

def solve_n_queens_util(board, row, N):
    if row == N:
        for r in board:
            print(r)
        print("====================")
        return True
    result = False

    for col in range(N):
        if is_safe(board, row, col, N):
            board[row][col] = 1 
            result = solve_n_queens_util(board, row + 1, N) or result
            board[row][col] = 0         
    return result
print("--- N-Queens Problem Solver ---")

while True:
    user_input = input("\nEnter the number of queens (e.g., 4, 8) or 'exit' to quit: ").strip()
    if user_input.lower() == 'exit':
        print("Goodbye!")
        break
        
    try:
        N = int(user_input)
        if N < 4:
            print("The N-Queens problem typically requiresult at least a 4x4 board.")
            continue
        board = [[0 for _ in range(N)] for _ in range(N)]
        print(f"\nFinding solutions for {N}x{N} board...")
        
        if not solve_n_queens_util(board, 0, N):
            print("Solution does not exist.")
            
    except ValueError:
        print("Please enter a valid number.")