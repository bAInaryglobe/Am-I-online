import platform
import subprocess
import time

def check_internet_connection():
    try:
        # Check host reachability
        host = "www.google.com"
        subprocess.run(["ping", "-c", "1", host], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
        return True
    except subprocess.CalledProcessError:
        return False

def get_network_type():
    try:
        result = subprocess.run(["networksetup", "-getinfo", "Wi-Fi"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True, text=True)
        if "Wi-Fi" in result.stdout:
            return "Wi-Fi"
        else:
            return "Ethernet"
    except subprocess.CalledProcessError:
        return "Unknown"

def main():
    os_name = platform.system()

    if os_name != "Darwin":
        print("This script is designed for macOS only.")
        return

    print("Operating System: macOS")
    print("Performing extensive checks...")

    start_time = time.time()
    is_online = check_internet_connection()
    end_time = time.time()

    print("Connection status: " + ("online" if is_online else "offline"))
    print("Network type:", get_network_type())
    print("Time online: {:.2f} seconds".format(end_time - start_time))

    breakdown_choice = input("Do you want a breakdown of the check results? (yes/no): ").strip().lower()

    if breakdown_choice == "yes":
        # Perform additional macOS-specific checks and store results in a dictionary
        check_results = {
            "Ping Google": subprocess.run(["ping", "-c", "1", "www.google.com"]).returncode,
            "Ping localhost": subprocess.run(["ping", "-c", "1", "localhost"]).returncode,
            # Add more macOS-specific checks here
        }

        print("\nBreakdown of check results:")
        for check, result in check_results.items():
            print(f"{check}: {'Success' if result == 0 else 'Failure'}")

if __name__ == "__main__":
    main()
