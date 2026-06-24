#!/usr/bin/env python3
"""
setup_venv.py
Cross-platform script to create a virtual environment, upgrade pip,
and install dependencies for the research projects.
Works on macOS, Linux (UNIX), and Windows.
"""

import os
import sys
import subprocess
import platform
import shutil

# Target directory for the virtual environment
VENV_DIR = ".venv"
REQUIREMENTS_FILE = "requirements.txt"


def print_step(message):
    print(f"\n=== {message} ===")


def check_python_version():
    """Ensure the Python version is 3.8 or higher."""
    major, minor = sys.version_info[:2]
    if (major, minor) < (3, 8):
        print(f"Error: Python 3.8+ is required. Current version is {major}.{minor}.", file=sys.stderr)
        sys.exit(1)
    print(f"Python version check passed: {sys.version.split()[0]}")


def create_venv():
    """Create the virtual environment using python -m venv."""
    print_step(f"Creating virtual environment in '{VENV_DIR}'...")
    if os.path.exists(VENV_DIR):
        print(f"Virtual environment directory '{VENV_DIR}' already exists. Skipping creation.")
        return

    try:
        # Run the venv creation command using the current Python executable
        subprocess.run([sys.executable, "-m", "venv", VENV_DIR], check=True)
        print("Virtual environment created successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to create virtual environment: {e}", file=sys.stderr)
        sys.exit(1)


def get_venv_executables():
    """Get the path to python and pip executables inside the venv based on the OS."""
    is_windows = platform.system() == "Windows"
    if is_windows:
        python_bin = os.path.join(VENV_DIR, "Scripts", "python.exe")
        pip_bin = os.path.join(VENV_DIR, "Scripts", "pip.exe")
    else:
        python_bin = os.path.join(VENV_DIR, "bin", "python")
        pip_bin = os.path.join(VENV_DIR, "bin", "pip")

    return python_bin, pip_bin


def upgrade_pip(python_bin):
    """Upgrade pip and setuptools inside the virtual environment."""
    print_step("Upgrading pip and setuptools inside the virtual environment...")
    try:
        subprocess.run([python_bin, "-m", "pip", "install", "--upgrade", "pip", "setuptools"], check=True)
        print("pip and setuptools upgraded successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to upgrade pip: {e}", file=sys.stderr)
        sys.exit(1)


def install_requirements(pip_bin):
    """Install dependencies from requirements.txt."""
    print_step(f"Installing dependencies from '{REQUIREMENTS_FILE}'...")
    if not os.path.exists(REQUIREMENTS_FILE):
        print(f"Error: '{REQUIREMENTS_FILE}' not found in the current directory.", file=sys.stderr)
        sys.exit(1)

    try:
        subprocess.run([pip_bin, "install", "-r", REQUIREMENTS_FILE], check=True)
        print("Dependencies installed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to install dependencies: {e}", file=sys.stderr)
        sys.exit(1)


def print_activation_instructions():
    """Print OS-specific instructions to activate the environment."""
    print_step("Environment Setup Complete!")
    os_name = platform.system()
    
    print("To activate the virtual environment, run the following command:")
    if os_name == "Windows":
        print("\n  For Command Prompt:")
        print(f"    {VENV_DIR}\\Scripts\\activate.bat")
        print("\n  For PowerShell:")
        print(f"    .\\{VENV_DIR}\\Scripts\\Activate.ps1")
        print("\n  For Git Bash / WSL:")
        print(f"    source {VENV_DIR}/Scripts/activate")
    else:
        print(f"\n    source {VENV_DIR}/bin/activate")
        
    print("\nTo launch Jupyter Notebook or Jupyter Lab:")
    print("  1. Activate the environment (using the appropriate command above)")
    print("  2. Run:")
    print("     jupyter notebook")
    print("\nHappy coding!")


def main():
    check_python_version()
    create_venv()
    python_bin, pip_bin = get_venv_executables()
    upgrade_pip(python_bin)
    install_requirements(pip_bin)
    print_activation_instructions()


if __name__ == "__main__":
    main()
