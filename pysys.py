import os
import xml.etree.ElementTree as ET
import subprocess
import time

class PySys:
    def __init__(self):
        self.obn_enabled = False
        self.version = self.get_version()

    def get_version(self):
        """ Reads the current version from version.txt """
        if os.path.exists("version.txt"):
            with open("version.txt", "r") as f:
                return f.read().strip()
        return "0.4demo"

    def update_version(self):
        """ Updates PySys version automatically """
        current_version = float(self.version.replace("demo", "").strip())
        next_version = current_version + 0.1
        if next_version >= 1.0:
            next_version = "1.0-beta"

        with open("version.txt", "w") as f:
            f.write(str(next_version))

        self.version = str(next_version)
        print(f"System updated to PySys v{self.version}!")

    def start(self):
        print(f"PySys v{self.version}")
        print('Use "pysys help" for a list of commands.')
        print("Starting PySys... (1 to 5 seconds)")
        time.sleep(2)
        self.command_loop()

    def command_loop(self):
        while True:
            command = input("pysys> ").strip()

            if command.startswith("pysys file new "):
                filename = command.replace("pysys file new ", "").strip()
                self.create_file(filename)
            elif command.startswith("pysys file edit "):
                filename = command.replace("pysys file edit ", "").strip()
                self.edit_file(filename)
            elif command.startswith("pysys run "):
                script = command.replace("pysys run ", "").strip()
                self.run_script(script)
            elif command.lower() == "pysys restart":
                self.restart_system()
            elif command.startswith("pysys load "):
                resource = command.replace("pysys load ", "").strip()
                self.load_resource(resource)
            elif command.lower() == "pysys status":
                self.system_status()
            elif command.lower() == "pysys check":
                self.system_check()
            elif command.lower() == "pysys log":
                self.view_logs()
            elif command.lower() == "pysys config":
                self.view_config()
            elif command.lower() == "pysys update":
                self.update_version()
            elif command.startswith("pysys remove "):
                package = command.replace("pysys remove ", "").strip()
                self.remove_package(package)
            elif command.startswith("pysys install pkg "):
                parts = command.split(" ")
                if len(parts) == 5 and parts[3] == "obn" and parts[4] == "false":
                    package_name = parts[2]
                    self.install_pysys_package(package_name)
                else:
                    print("Invalid syntax. Use: pysys install pkg <PkgName> obn false")
            elif command.lower() == "pysys clean":
                self.clean_temp_files()
            elif command.startswith("pysys set obn "):
                status = command.replace("pysys set obn ", "").strip()
                self.set_obn_status(status)
            elif command.startswith("pysys obn pkg "):
                package = command.replace("pysys obn pkg ", "").strip()
                self.install_obn_package(package)
            elif command.lower() == "pysys help":
                self.show_help()
            else:
                print(f"Unknown command: {command}")

    # FILE MANAGEMENT FUNCTIONS
    def create_file(self, filename):
        if not filename:
            print("Error 700-7000: FileName cannot be empty")
            return
        print(f"Creating file: {filename}")
        with open(filename, "w") as f:
            f.write("")
        print("File created successfully.")

    def edit_file(self, filename):
        print(f"Opening file for editing: {filename}")

    # SYSTEM COMMANDS
    def run_script(self, script):
        print(f"Executing script: {script}")

    def restart_system(self):
        print("Restarting system...")
        time.sleep(2)
        print("System restarted successfully.")

    def load_resource(self, resource):
        print(f"Loading: {resource}")

    def system_status(self):
        print("Checking system status...")
        time.sleep(1)
        print("System is running normally.")

    def system_check(self):
        print("Running diagnostics...")
        time.sleep(2)
        print("No issues found.")

    def view_logs(self):
        print("Displaying logs...")

    def view_config(self):
        print("Opening system configuration...")

    def clean_temp_files(self):
        print("Cleaning temporary files...")
        time.sleep(2)
        print("Cleanup complete.")

    # PACKAGE MANAGEMENT
    def remove_package(self, package):
        print(f"Removing package: {package}")
        time.sleep(2)
        print(f"Package {package} removed successfully.")

    def install_pysys_package(self, package_name):
        package_path = f"pysys_packages/{package_name}"
        
        metadata_file = f"{package_path}/metadata.xml"
        install_script = f"{package_path}/install.py"

        if not os.path.exists(metadata_file):
            print(f"Error: Metadata file missing for package '{package_name}'.")
            return

        # Load package metadata
        tree = ET.parse(metadata_file)
        root = tree.getroot()
        package_name = root.find("name").text
        version = root.find("version").text

        print(f"Installing {package_name} v{version} via PySys-branded package system...")

        if os.path.exists(install_script):
            subprocess.run(["python", install_script])
        else:
            print("Warning: No install.py script found, dependencies may not be auto-installed.")

        print("Package installation complete!")

    # OBN PACKAGE MANAGEMENT
    def set_obn_status(self, status):
        if status.lower() == "true":
            self.obn_enabled = True
            print("OBN Package enabled.")
        elif status.lower() == "false":
            self.obn_enabled = False
            print("OBN Package disabled.")
        else:
            print("Error: Invalid value. Use 'pysys set obn true' or 'pysys set obn false'.")

    def install_obn_package(self, package_name):
        package_path = f"obn_packages/{package_name}"
        
        metadata_file = f"{package_path}/metadata.xml"
        install_script = f"{package_path}/install.py"

        if not os.path.exists(metadata_file):
            print(f"Error: Metadata file missing for package '{package_name}'.")
            return

        if not self.obn_enabled:
            print("Error: OBN Package is not enabled. Use 'pysys set obn true' first.")
            return

        # Load package metadata
        tree = ET.parse(metadata_file)
        root = tree.getroot()
        package_name = root.find("name").text
        version = root.find("version").text

        print(f"Installing {package_name} v{version} via OBN Package...")

        if os.path.exists(install_script):
            subprocess.run(["python", install_script])
        else:
            print("Warning: No install.py script found, dependencies may not be auto-installed.")

        print("Package installation complete!")

    # HELP COMMAND
    def show_help(self):
        print("Available commands:")
        print(" - pysys file new <filename>")
        print(" - pysys file edit <filename>")
        print(" - pysys run <script.py>")
        print(" - pysys restart")
        print(" - pysys load <resource>")
        print(" - pysys status")
        print(" - pysys check")
        print(" - pysys log")
        print(" - pysys config")
        print(" - pysys update")
        print(" - pysys remove <package>")
        print(" - pysys install pkg <PkgName> obn false")
        print(" - pysys clean")
        print(" - pysys set obn <true/false>")
        print(" - pysys obn pkg <package>")
        print(" - pysys help")

# Run PySys
if __name__ == "__main__":
    pysys = PySys()
    pysys.start()
