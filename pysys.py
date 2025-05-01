import argparse
import os
import subprocess
import sys
import shutil

def list_files(args):
    """Lists files in the specified directory or current directory if not specified."""
    path = args.path if args.path else "."
    try:
        files = os.listdir(path)
        print("\n".join(files))
    except FileNotFoundError:
        print(f"Error: Directory '{path}' not found.")

def show_system_info(args):
    """Displays basic system information."""
    try:
        subprocess.run(["uname", "-a"])
    except FileNotFoundError:
        print("Error: 'uname' command not available on this system.")

def current_directory(args):
    """Displays the current working directory."""
    print(os.getcwd())

def execute_command(args):
    """Executes a system command."""
    try:
        subprocess.run(args.command, shell=True)
    except Exception as e:
        print(f"Error executing command: {e}")

def install_package(args):
    """Installs a Python package from pip or GitHub."""
    if args.source == "pip":
        try:
            subprocess.run([sys.executable, "-m", "pip", "install", args.package])
        except Exception as e:
            print(f"Error installing package via pip: {e}")
    elif args.source == "github":
        repo_url = "repo-link"  # Replace with actual repository URL
        clone_path = os.path.join(os.getcwd(), args.package)
        try:
            subprocess.run(["git", "clone", repo_url, clone_path])
            os.chdir(clone_path)
            subprocess.run([sys.executable, "-m", "pip", "install", "."])
        except Exception as e:
            print(f"Error cloning or installing package from GitHub: {e}")
    else:
        print("Invalid source. Use 'pip' or 'github'.")

def uninstall_package(args):
    """Uninstalls a Python package from pip or removes a GitHub-cloned package."""
    if args.source == "pip":
        try:
            subprocess.run([sys.executable, "-m", "pip", "uninstall", "-y", args.package])
        except Exception as e:
            print(f"Error uninstalling package via pip: {e}")
    elif args.source == "github":
        package_path = os.path.join(os.getcwd(), args.package)
        try:
            if os.path.exists(package_path):
                shutil.rmtree(package_path)
                print(f"Successfully removed '{args.package}' from system.")
            else:
                print(f"Error: '{args.package}' not found.")
        except Exception as e:
            print(f"Error removing package: {e}")
    else:
        print("Invalid source. Use 'pip' or 'github'.")

def main():
    parser = argparse.ArgumentParser(description="PySys - A simple system command CLI")
    subparsers = parser.add_subparsers(dest="command")

    # 'pyls' command
    ls_parser = subparsers.add_parser("pyls", help="List files in a directory")
    ls_parser.add_argument("path", nargs="?", default=".", help="Path of the directory")

    # 'pysysinfo' command
    sysinfo_parser = subparsers.add_parser("pysysinfo", help="Show system information")

    # 'pypwd' command
    pwd_parser = subparsers.add_parser("pypwd", help="Show current directory")

    # 'pyexec' command
    exec_parser = subparsers.add_parser("pyexec", help="Execute a system command")
    exec_parser.add_argument("command", help="Command to execute")

    # 'pyinstall' command
    install_parser = subparsers.add_parser("pyinstall", help="Install a Python package")
    install_parser.add_argument("package", help="Name of the package to install")
    install_parser.add_argument("source", choices=["pip", "github"], help="Installation source: 'pip' or 'github'")

    # 'pyuninstall' command
    uninstall_parser = subparsers.add_parser("pyuninstall", help="Uninstall a Python package")
    uninstall_parser.add_argument("package", help="Name of the package to uninstall")
    uninstall_parser.add_argument("source", choices=["pip", "github"], help="Uninstallation source: 'pip' or 'github'")

    args = parser.parse_args()

    if args.command == "pyls":
        list_files(args)
    elif args.command == "pysysinfo":
        show_system_info(args)
    elif args.command == "pypwd":
        current_directory(args)
    elif args.command == "pyexec":
        execute_command(args)
    elif args.command == "pyinstall":
        install_package(args)
    elif args.command == "pyuninstall":
        uninstall_package(args)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
