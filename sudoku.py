class SudokuGame:
    def __init__(self):
        # Initialize the game and its data structures
        self.grid = [[0] * 9 for _ in range(9)]
    
    def reset(self):
        # Reset the game to its initial state
        self.grid = [[0] * 9 for _ in range(9)]
    
    def is_valid_move(self, row, col, num):
        # Check if a move is valid or not
        if self.grid[row][col] != 0:
            return False
        
        # Check row and column
        for i in range(9):
            if self.grid[row][i] == num or self.grid[i][col] == num:
                return False
        
        # Check 3x3 square
        start_row = (row // 3) * 3
        start_col = (col // 3) * 3
        for i in range(3):
            for j in range(3):
                if self.grid[start_row + i][start_col + j] == num:
                    return False
        
        return True
    
    def make_move(self, row, col, num):
        # Make a move by inserting a number into the grid
        if self.is_valid_move(row, col, num):
            self.grid[row][col] = num
            return True
        return False
    
    def get_suggested_move(self):
        # Generate a suggested move after 3 consecutive invalid responses
        invalid_count = 0
        for row in range(9):
            for col in range(9):
                if self.grid[row][col] == 0:
                    for num in range(1, 10):
                        if self.is_valid_move(row, col, num):
                            return row, col, num
                    invalid_count += 1
                    if invalid_count >= 3:
                        break
            if invalid_count >= 3:
                break
        return None
    
    def is_game_over(self):
        # Check if the Sudoku puzzle has been solved
        for row in range(9):
            for col in range(9):
                if self.grid[row][col] == 0:
                    return False
        return True
#Coded by Neelanjan
