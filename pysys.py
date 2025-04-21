import argparse
import psutil
import yaml
import os
import subprocess
import logging
import socket
from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt

# Initialize rich console and logging
console = Console()
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# Load Configuration
def load_config(file_path="config.yaml"):
    if os.path.exists(file_path):
        with open(file_path, "r") as file:
            return yaml.safe_load(file)
    return {"settings": {"theme": "dark", "log_level": "info", "obn_enabled": False}}

config = load_config()

# Save Configuration
def save_config(config, file_path="config.yaml"):
    with open(file_path, "w") as file:
        yaml.dump(config, file)

# Enable OBN Mode
def enable_obn():
    config["settings"]["obn_enabled"] = True
    save_config(config)
    console.print("[yellow]OBN Enabled[/yellow]")
    logging.info("OBN Mode activated.")

# Install Package (Python)
def install_package(package_name):
    try:
        console.print(f"[bold green]Installing Python package: {package_name}[/bold green]")
        subprocess.run(["pip", "install", package_name], check=True)
        console.print(f"[green]Package '{package_name}' installed successfully![/green]")
        logging.info(f"Installed package: {package_name}")
    except subprocess.CalledProcessError:
        console.print(f"[red]Failed to install '{package_name}'. Check if the package name is correct.[/red]")

# Install OBN Package
def install_obn_package(package_name):
    if not config["settings"]["obn_enabled"]:
        console.print("[red]OBN is not enabled! Use 'pysys set obn true' first.[/red]")
        return

    try:
        console.print(f"[bold green]Installing OBN package: {package_name}[/bold green]")
        subprocess.run(["obn-cli", "install", package_name], check=True)  # Replace with actual OBN command
        console.print(f"[green]OBN Package '{package_name}' installed successfully![/green]")
        logging.info(f"Installed OBN package: {package_name}")
    except subprocess.CalledProcessError:
        console.print(f"[red]Failed to install '{package_name}'. Ensure OBN is installed.[/red]")

def main():
    parser = argparse.ArgumentParser(description="PySys - System Utility Tool with OBN Support")
    parser.add_argument("--pysys-info", action="store_true", help="Show system info")
    parser.add_argument("--pysys-processes", action="store_true", help="List running processes")
    parser.add_argument("--pysys-install", type=str, help="Install a Python package using pip")
    parser.add_argument("--pysys-set-obn", action="store_true", help="Enable OBN mode")
    parser.add_argument("--pysys-obn-install", type=str, help="Install an OBN package")

    args = parser.parse_args()

    if args.pysys_info:
        system_info()
    elif args.pysys_processes:
        list_processes()
    elif args.pysys_install:
        install_package(args.pysys_install)
    elif args.pysys_set_obn:
        enable_obn()
    elif args.pysys_obn_install:
        install_obn_package(args.pysys_obn_install)
    else:
        console.print("[yellow]No command provided. Use --help to see available options.[/yellow]")

if __name__ == "__main__":
    main()
