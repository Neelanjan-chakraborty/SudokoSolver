from flask import Flask, request
from flask_cors import CORS
from flask import jsonify
import random

#Coded by Neelanjan
app = Flask(__name__)
cors=CORS(app,resources={r"/*": {"origins": "*"}})

# Import the SudokuGame class from sudoku.py ,so if it does exist in the same folder we immport it here
from sudoku import SudokuGame

sudoku_game = SudokuGame()
@app.route('/')
#def index():
#    return 'Welcome to the Sudoku API' lol
def is_game_over(self):
    #To Check if the Sudoku puzzle is solved
    for i in range(9):
        for j in range(9):
            if self.grid[i][j] == 0:
                return False
    return True


def generate_sudoku_grid():
    grid = [[0 for _ in range(9)] for _ in range(9)]
    solve_sudoku(grid)
    remove_cells(grid)
    return grid

def remove_cells(grid):
    # Determine the number of cells to remove (adjust this value as desired)
    cells_to_remove = 40

    # Randomly remove cells from the grid for challenge
    for _ in range(cells_to_remove):
        row = random.randint(0, 8)
        col = random.randint(0, 8)
        grid[row][col] = " "


def solve_sudoku(grid):
    empty_cells = find_empty_cells(grid)
    if not empty_cells:
        return True

    row, col = empty_cells[0]
    for num in range(1, 10):
        if is_valid_move(grid, row, col, num):
            grid[row][col] = num
            if solve_sudoku(grid):
                return True
            grid[row][col] = 0

    return False

def find_empty_cells(grid):
    empty_cells = []
    for row in range(9):
        for col in range(9):
            if grid[row][col] == 0:
                empty_cells.append((row, col))
    return empty_cells

def is_valid_move(grid, row, col, num):
    # Check if the number already exists in the same row
    for i in range(9):
        if grid[row][i] == num:
            return False

    # Check if the number already exists in the same column
    for i in range(9):
        if grid[i][col] == num:
            return False

    # Check if the number already exists in the same 3x3 square
    start_row = (row // 3) * 3
    start_col = (col // 3) * 3
    for i in range(3):
        for j in range(3):
            if grid[start_row + i][start_col + j] == num:
                return False

    return True

consecutive_invalid_responses = 0


@app.route('/start', methods=['POST'])
def start_game():
    # so this well Reset the game and start a fresh Sudoku game
    sudoku_game.reset()
    # Generate the Sudoku grid and return it
    sudoku_grid = generate_sudoku_grid()
    response = jsonify({"sudoku": sudoku_grid})  # Wrap the Sudoku grid in a dictionary
    response.headers.add("Access-Control-Allow-Origin", "*")  # Allow requests from any origin
    return response


@app.route('/move', methods=['POST'])
def make_move():
    global consecutive_invalid_responses  

    # Handle move insertion by accepting the row, column, and number in the request body
    data = request.get_json()
    row = data.get('row')
    col = data.get('col')
    num = data.get('num')

    if row is None or col is None or num is None:
        return "Invalid request. Please provide row, col, and num in the request body.", 400

    if not isinstance(row, int) or not isinstance(col, int) or not isinstance(num, int):
        return 'Invalid request. Row, col, and num must be integers.'

    result = 'Invalid'

    if result == 'Invalid':
        #umm this will Generate a suggested move
        suggested_move = sudoku_game.get_suggested_move()
        if suggested_move:
            suggested_row, suggested_col, suggested_num = suggested_move
            sudoku_game.make_move(suggested_row, suggested_col, suggested_num)
            result = f'Suggested move: ({suggested_row}, {suggested_col}, {suggested_num})'
            consecutive_invalid_responses = 0  # Reset the consecutive invalid responses counter
        else:
            consecutive_invalid_responses += 1  # Increment the consecutive invalid responses counter

    if consecutive_invalid_responses >= 3:
        # umm this will Generate another suggested move
        suggested_move = sudoku_game.get_suggested_move()
        if suggested_move:
            suggested_row, suggested_col, suggested_num = suggested_move
            sudoku_game.make_move(suggested_row, suggested_col, suggested_num)
            result = f'Suggested move: ({suggested_row}, {suggested_col}, {suggested_num})'

    if sudoku_game.is_game_over():
        result = 'Game Over: Sudoku puzzle solved!'

    return result

app.run(debug=True)
cors = CORS(app)

