import os
import platform
import datetime
import subprocess
import readline

# List of built-in commands for tab-completion
COMMANDS = ['help', 'exit', 'clear', 'sysinfo', 'date', 'ls', 'pwd', 'mkdir', 'rmdir', 'history', 'calc']

def completer(text, state):
    """Suggest and complete built-in commands based on user input."""
    options = [cmd for cmd in COMMANDS if cmd.startswith(text)]
    if state < len(options):
        return options[state]
    else:
        return None

# Setup tab-completion for built-in commands
readline.set_completer(completer)
readline.parse_and_bind("tab: complete")

# Use a history file to store command history between sessions.
HISTORY_FILE = "pysys_history.txt"
try:
    readline.read_history_file(HISTORY_FILE)
except FileNotFoundError:
    pass

def clear_screen():
    """Clear the terminal screen based on the operating system."""
    if os.name == 'nt':  # Windows
        os.system('cls')
    else:  # Unix/Linux/MacOS
        os.system('clear')

def get_sys_info():
    """Return a string with detailed information about the system."""
    info = [
        f"System        : {platform.system()}",
        f"Node Name     : {platform.node()}",
        f"Release       : {platform.release()}",
        f"Version       : {platform.version()}",
        f"Machine       : {platform.machine()}",
        f"Processor     : {platform.processor()}",
        f"Python Version: {platform.python_version()}"
    ]
    return "\n".join(info)

def print_help():
    """Display help message listing all available commands."""
    help_text = """
Available commands:
  help       - Show this help message.
  exit       - Exit pysys.
  clear      - Clear the terminal screen.
  sysinfo    - Display system information.
  date       - Display the current date and time.
  ls         - List files in the current directory.
  pwd        - Display current working directory.
  mkdir      - Create a new directory. Usage: mkdir <directory_name>
  rmdir      - Remove a directory. Usage: rmdir <directory_name>
  history    - Display the command history.
  calc       - Evaluate a simple arithmetic expression. Usage: calc <expression>
  
Any command not recognized as a built-in is passed to the operating system shell.
    """
    print(help_text)

def show_date():
    """Print the current date and time."""
    now = datetime.datetime.now()
    print(now.strftime("%Y-%m-%d %H:%M:%S"))

def execute_external_command(command):
    """Pass non-built-in commands to the system shell."""
    try:
        subprocess.run(command, shell=True)
    except Exception as e:
        print("Error executing command:", e)

def list_directory():
    """List files and directories in the current working directory."""
    try:
        files = os.listdir('.')
        for f in files:
            print(f)
    except Exception as e:
        print("Error listing directory:", e)

def print_pwd():
    """Print the current working directory."""
    try:
        print(os.getcwd())
    except Exception as e:
        print("Error retrieving current directory:", e)

def make_directory(args):
    """Create a directory. Usage: mkdir <directory_name>"""
    if len(args) < 2:
        print("Usage: mkdir <directory_name>")
    else:
        try:
            os.mkdir(args[1])
            print(f"Directory '{args[1]}' created.")
        except Exception as e:
            print("Error creating directory:", e)

def remove_directory(args):
    """Remove a directory. Usage: rmdir <directory_name>"""
    if len(args) < 2:
        print("Usage: rmdir <directory_name>")
    else:
        try:
            os.rmdir(args[1])
            print(f"Directory '{args[1]}' removed.")
        except Exception as e:
            print("Error removing directory:", e)

def show_history():
    """Display the list of commands entered during the session."""
    history_length = readline.get_current_history_length()
    for i in range(1, history_length + 1):
        print(f"{i}: {readline.get_history_item(i)}")

def calculate_expression(args):
    """Evaluate a simple arithmetic expression provided by the user.
    
    Usage: calc <expression>
    """
    if len(args) < 2:
        print("Usage: calc <expression>")
    else:
        expr = " ".join(args[1:])
        try:
            # Evaluate in a restricted namespace for safety reasons.
            result = eval(expr, {"__builtins__": None}, {})
            print(result)
        except Exception as e:
            print("Error evaluating expression:", e)

def main():
    # Boot banner as requested
    print("PythonSystem [0.1.0.00000]")
    print("2025 HomebrewHorizon\n")
    
    while True:
        try:
            user_input = input("pysys> ").strip()
            if not user_input:
                continue
            
            # Add command to history for up-arrow recall
            readline.add_history(user_input)
            
            # Split input into command parts
            parts = user_input.split()
            command = parts[0].lower()
            
            # Check for built-in commands
            if command == "exit":
                print("Exiting pysys. Goodbye!")
                break
            elif command == "help":
                print_help()
            elif command == "clear":
                clear_screen()
            elif command == "sysinfo":
                print(get_sys_info())
            elif command == "date":
                show_date()
            elif command == "ls":
                list_directory()
            elif command == "pwd":
                print_pwd()
            elif command == "mkdir":
                make_directory(parts)
            elif command == "rmdir":
                remove_directory(parts)
            elif command == "history":
                show_history()
            elif command == "calc":
                calculate_expression(parts)
            else:
                # Fall back to system shell execution
                execute_external_command(user_input)
        except KeyboardInterrupt:
            print("\nTerminated by user. Exiting pysys.")
            break

    # On exit, save the history so that it is available next time.
    try:
        readline.write_history_file(HISTORY_FILE)
    except Exception as e:
        print("Error saving history:", e)

if __name__ == "__main__":
    main()
