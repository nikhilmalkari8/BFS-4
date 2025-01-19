def updateBoard(board, click):
    rows, cols = len(board), len(board[0])
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
    
    def countMines(x, y):
        """Count the number of mines adjacent to (x, y)."""
        count = 0
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols and board[nx][ny] == 'M':
                count += 1
        return count

    def dfs(x, y):
        """Reveal cells recursively starting from (x, y)."""
        if not (0 <= x < rows and 0 <= y < cols) or board[x][y] != 'E':
            return
        
        mines = countMines(x, y)
        if mines > 0:
            board[x][y] = str(mines)
        else:
            board[x][y] = 'B'
            for dx, dy in directions:
                dfs(x + dx, y + dy)
    
    x, y = click
    if board[x][y] == 'M':
        board[x][y] = 'X'
    else:
        dfs(x, y)
    
    return board
