import os
import xml.etree.ElementTree as ET
import subprocess
import time

class PySys:
    def __init__(self):
        self.obn_enabled = False
        self.version = self.get_version()

    def get_version(self):
        """ Reads the current version from version.txt or throws an error if missing """
        if os.path.exists("version.txt"):
            with open("version.txt", "r") as f:
                return f.read().strip()
        print("Error: version.txt not found! Creating default version.")
        with open("version.txt", "w") as f:
            f.write("0.4demo")
        return "0.4demo"

    def update_version(self):
        """ Updates PySys version automatically """
        try:
            current_version = float(self.version.replace("demo", "").strip())
            next_version = current_version + 0.1
            if next_version >= 1.0:
                next_version = "1.0-beta"

            with open("version.txt", "w") as f:
                f.write(str(next_version))

            self.version = str(next_version)
            print(f"System updated to PySys v{self.version}!")
        except ValueError:
            print("Error: Invalid version format in version.txt")

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
            elif command.lower() == "pysys obn list":
                self.list_obn_packages()
            elif command.startswith("pysys obn remove "):
                package = command.replace("pysys obn remove ", "").strip()
                self.remove_obn_package(package)
            elif command.startswith("pysys obn update "):
                package = command.replace("pysys obn update ", "").strip()
                self.update_obn_package(package)
            elif command.lower() == "pysys obn reset":
                self.reset_obn()
            elif command.lower() == "pysys obn check":
                self.check_obn_integrity()
            elif command.lower() == "pysys obn scan":
                self.scan_obn_updates()
            elif command.lower() == "pysys help":
                self.show_help()
            else:
                print(f"Unknown command: {command}")

    # OBN PACKAGE COMMANDS
    def list_obn_packages(self):
        print("Listing installed OBN packages...")
        # Mock implementation
        installed_packages = ["nds-src", "sys-utils", "net-manager"]
        for pkg in installed_packages:
            print(f" - {pkg}")

    def remove_obn_package(self, package):
        print(f"Removing OBN package: {package}")
        time.sleep(2)
        print(f"Package {package} removed successfully.")

    def update_obn_package(self, package):
        print(f"Updating OBN package: {package}")
        time.sleep(2)
        print(f"{package} updated successfully.")

    def reset_obn(self):
        print("Resetting all OBN package settings...")
        time.sleep(2)
        print("OBN settings reset successfully.")

    def check_obn_integrity(self):
        print("Checking OBN package integrity...")
        time.sleep(2)
        print("All OBN packages verified successfully.")

    def scan_obn_updates(self):
        print("Scanning for OBN package updates...")
        time.sleep(2)
        print("Available updates: nds-src v1.1, net-manager v2.3")

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
        print(" - pysys obn list")
        print(" - pysys obn remove <package>")
        print(" - pysys obn update <package>")
        print(" - pysys obn reset")
        print(" - pysys obn check")
        print(" - pysys obn scan")
        print(" - pysys help")

# Run PySys
if __name__ == "__main__":
    pysys = PySys()
    pysys.start()
