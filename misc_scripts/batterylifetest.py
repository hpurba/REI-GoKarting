# Run: python3 batterylifetest.py
# Check the file: cat runtime_log.txt

import time
from datetime import datetime, timedelta

# Define the log file name
LOG_FILE = "runtime_log.txt"

def log_runtime(start_time):
    """Logs the elapsed time to the log file."""
    elapsed_time = datetime.now() - start_time
    with open(LOG_FILE, "a") as file:
        file.write(f"Program running for: {elapsed_time} (hh:mm:ss.ms) at {datetime.now()}\n")

if __name__ == "__main__":
    # Record the start time of the program
    start_time = datetime.now()
    
    print(f"Program started at: {start_time}")
    print(f"Logging runtime to {LOG_FILE} every minute...")

    try:
        while True:
            log_runtime(start_time)
            time.sleep(60)  # Wait for 1 minute (60 seconds)
    except KeyboardInterrupt:
        print("Program interrupted by user.")
        print("Exiting...")
