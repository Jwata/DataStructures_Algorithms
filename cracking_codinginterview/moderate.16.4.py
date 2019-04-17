def has_won(board, n):
    # check each row
    for i in range(n):
        sum_row = sum(board[i])
        if sum_row == 0 or sum_row == n:
            return True

    # check each column
    for i in range(n):
        sum_col = 0
        for j in range(n): 
            sum_col += board[j][i]
        if sum_col == 0 or sum_col == n:
            return True

    # check diagonals
    sum_diag = 0
    for i in range(n):
        sum_diag += board[i][i]
    if sum_diag == 0 or sum_diag == n:
        return True

    sum_diag = 0
    for i in range(n):
        sum_diag += board[i][n-i-1]
    if sum_diag == 0 or sum_diag == n:
        return True

    return False

board = [[0, 1, 0], \
         [0, 1, 1], \
         [0, 0, 1]]
print(has_won(board, 3)) # True

board = [[0, 1, 0], \
         [1, 1, 0], \
         [0, 0, 1]]
print(has_won(board, 3)) # False
