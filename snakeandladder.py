from collections import deque

def snakesAndLadders(board):
    n = len(board)
    
    def get_position(num):
        """Convert 1D position to 2D coordinates."""
        quot, rem = divmod(num - 1, n)
        row = n - 1 - quot
        col = rem if row % 2 != n % 2 else n - 1 - rem
        return row, col

    # BFS initialization
    visited = set()
    queue = deque([(1, 0)])  # (current square, number of moves)

    while queue:
        current, moves = queue.popleft()
        if current == n * n:
            return moves
        
        for roll in range(1, 7):  # Roll the dice
            next_square = current + roll
            if next_square > n * n:
                break
            
            r, c = get_position(next_square)
            if board[r][c] != -1:
                next_square = board[r][c]  # Follow snake or ladder
            
            if next_square not in visited:
                visited.add(next_square)
                queue.append((next_square, moves + 1))
    
    return -1  # If destination is not reachable
