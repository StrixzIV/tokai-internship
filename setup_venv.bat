@echo off
rem Wrapper script to run setup_venv.py on Windows

cd /d "%~dp0"

where python >nul 2>nul
if %errorlevel% equ 0 (
    python setup_venv.py
) else (
    echo Error: Python was not found on your system. Please install Python 3 and try again.
    pause
    exit /b 1
)
