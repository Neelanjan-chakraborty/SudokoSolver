# SudokoSolver
The Sudoku Solver project is a web-based app with API and GUI components, allowing users to play and solve Sudoku puzzles interactively. It features error handling, move suggestions, and continuous gameplay until the puzzle is solved.
1. Install Python: Ensure that you have Python installed on your machine. You can download Python from the [official website](https://www.python.org) and follow the installation instructions.

2. Install required packages: Open a command prompt or terminal and navigate to the project directory. Run the following command to install the required packages:

```
pip install flask flask_cors
```


3. Run the server: In the command prompt or terminal, navigate to the project directory and run the following command to start the Flask server:

```
python app.py
```


This will start the server on `http://localhost:5000`.

4. Test the API using cURL: Open a new command prompt or terminal window and run the following cURL commands to interact with the API:

- To start a new Sudoku game:
  ```
  curl -X POST http://localhost:5000/start
  ```

- To make a move on the Sudoku board:
  ```
  curl -X POST -H "Content-Type: application/json" -d "{\"row\": 0, \"col\": 0, \"num\": 5}" http://localhost:5000/move
  ```

You can modify the values in the JSON payload (`row`, `col`, `num`) to make moves on different cells.

Note: Make sure the server is running (`app.py`) before making these API calls.

5. Test the GUI (optional): If you want to test the GUI interface, you can run the `run.bat` file. This will open the GUI application, allowing you to interact with the Sudoku solver visually.

Note: The GUI relies on the Flask server being running in the background.



