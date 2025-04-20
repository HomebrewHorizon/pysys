import time

class PySys:
    def __init__(self):
        self.obn_enabled = False

    def start(self):
        print("PySys v0.1demo")
        print('Use "pysys help" for a list of commands.')
        print("Starting PySys... (1 to 5 seconds)")
        time.sleep(2)  # Simulating startup delay
        self.command_loop()

    def command_loop(self):
        while True:
            command = input("pysys> ").strip()
            if command.lower() == "pysys exit":
                print("Exiting PySys...")
                break
            elif command.lower() == "pysys set obn true":
                self.enable_obn()
            elif command.startswith("pysys obn pkg "):
                package = command.replace("pysys obn pkg ", "").strip()
                self.install_package(package)
            else:
                print(f"Unknown command: {command}")

    def enable_obn(self):
        print("Enabling OBN Package....")
        time.sleep(1)
        self.obn_enabled = True
        print("Done.")
        print('Use "pysys obn pkg <package>" to install a package.')

    def install_package(self, package_name):
        if not self.obn_enabled:
            print("Error: OBN Package is not enabled. Use 'pysys set obn true' first.")
            return
        print(f"Installing {package_name} via OBN Package...")
        time.sleep(2)  # Simulating installation delay
        print("Download Complete!")

# Run PySys
if __name__ == "__main__":
    pysys = PySys()
    pysys.start()
