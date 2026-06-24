#!/bin/bash
# Wrapper script to run setup_venv.py on macOS/Linux (UNIX)

# Make sure we are in the directory containing this script
cd "$(dirname "$0")"

# Check if python3 is available, fallback to python
if command -v python3 &>/dev/null; then
    python3 setup_venv.py
elif command -v python &>/dev/null; then
    python setup_venv.py
else
    echo "Error: Python was not found on your system. Please install Python 3 and try again."
    exit 1
fi
