def solver(board, r, c):
    if r == 9:
        return True
    if board[r][c] != 0:
        if c == 8:
            return solver(board, r + 1, 0)
        else:
            return solver(board, r, c + 1)

    for num in range(1, 10):
        if canFit(board, r, c, num):
            board[r][c] = num
            if c == 8:
                if solver(board, r + 1, 0):
                    return True
            else:
                if solver(board, r, c + 1):
                    return True
            board[r][c] = 0
    return False


def canFit(board, r, c, n):
    for i in range(9):
        if board[r][i] == n or board[i][c] == n:
            return False
        nr = 3 * (r // 3) + i // 3
        nc = 3 * (c // 3) + i % 3
        if board[nr][nc] == n:
            return False
    return True


def printer(board):
    for i in range(9):
        if i % 3 == 0:
            print(" ---------------------------")
        for j in range(9):
            if j % 3 == 0:
                print(" | ", end="")
            if board[i][j] == 0:
                print("  ", end="")
            else:
                print(f"{board[i][j]} ", end="")
        print("|")
    print(" ---------------------------")


if __name__ == "__main__":
    board = [[0 for _ in range(9)] for _ in range(9)]

    print("Enter the 9x9 Sudoku board (use 0 for empty cells):")
    for i in range(9):
        row = list(map(int, input().split()))
        if len(row) != 9:
            print("⚠️ Each row must have exactly 9 numbers!")
            exit(1)
        for j in range(9):
            if row[j] < 0 or row[j] > 9:
                print("⚠️ Please enter numbers between 0–9 only!")
                exit(1)
            board[i][j] = row[j]

    print("\nYour Sudoku board:")
    printer(board)

    if solver(board, 0, 0):
        print("✅ Solution for your Sudoku board:")
        printer(board)
    else:
        print("❌ No valid solution found. Something is wrong with the input.")
