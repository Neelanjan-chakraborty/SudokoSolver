@echo off

REM Start the Flask API server
start /B python.exe app.py

REM Wait for the server to start
timeout /t 5 >nul

REM Start the Tkinter GUI app
start /B python.exe gui.py
