import tkinter as tk
import requests
from tkinter import messagebox

API_URL = 'http://localhost:5000'  # Update with your API URL

class SudokuGUI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Sudoku Solver")

        self.sudoku_grid = [[tk.StringVar() for _ in range(9)] for _ in range(9)]

        self.create_grid()

        self.start_game_button = tk.Button(self.window, text="Start Game", command=self.start_game)
        self.start_game_button.grid(row=9, column=0, columnspan=9)

        self.make_move_button = tk.Button(self.window, text="Make Move", command=self.make_move)
        self.make_move_button.grid(row=10, column=0, columnspan=9)

    def create_grid(self):
        for i in range(9):
            for j in range(9):
                entry = tk.Entry(self.window, textvariable=self.sudoku_grid[i][j], width=5)
                entry.grid(row=i, column=j)

    def start_game(self):
        response = requests.post(f"{API_URL}/start")
        if response.status_code == 200:
            sudoku_data = response.json()
            for i in range(9):
                for j in range(9):
                    self.sudoku_grid[i][j].set(sudoku_data['sudoku'][i][j])
        else:
            print("Error starting the game.")

    def make_move(self):
        row_data = []
        for i in range(9):
            for j in range(9):
                value = self.sudoku_grid[i][j].get()
                if value.strip() == '':
                    row_data.append(0)  # Use 0 for empty cells
                else:
                    try:
                        row_data.append(int(value))
                    except ValueError:
                        messagebox.showerror('Invalid Move', 'Invalid move! Please enter a valid number.')
                        return
        move = {'row': 0, 'col': 0, 'num': row_data}  # Update with your move data
        response = requests.post(f"{API_URL}/move", json=move)
        if response.status_code == 200:
            try:
                result = response.json()
                if result['valid']:
                    self.display_result(result['message'])
                else:
                    messagebox.showerror('Invalid Move', 'Invalid move! The digits are repeated.')
            except ValueError:            	
                print(response.content)  # Print response content for debugging
                messagebox.showerror('Error', 'Error decoding the server response.')
        else:
            messagebox.showerror('Error', 'Error making the move.')


    def display_result(self, result):
        # Display the result in the GUI
        pass
 
    def run(self):
        self.window.mainloop()


if __name__ == '__main__':
    gui = SudokuGUI()
    gui.run()
