import psutil
import logging
import time
from datetime import datetime

# Configure logging
logging.basicConfig(filename='system_health.log', level=logging.INFO, format='%(asctime)s %(levelname)s: %(message)s')

# Define thresholds
CPU_THRESHOLD = 80
MEMORY_THRESHOLD = 80
DISK_THRESHOLD = 80
PROCESS_COUNT_THRESHOLD = 300  # Example threshold for running processes

def check_cpu_usage():
    cpu_usage = psutil.cpu_percent(interval=1)
    if cpu_usage > CPU_THRESHOLD:
        logging.warning(f"High CPU usage detected: {cpu_usage}%")
    return cpu_usage

def check_memory_usage():
    memory_info = psutil.virtual_memory()
    memory_usage = memory_info.percent
    if memory_usage > MEMORY_THRESHOLD:
        logging.warning(f"High Memory usage detected: {memory_usage}%")
    return memory_usage

def check_disk_usage():
    disk_info = psutil.disk_usage('/')
    disk_usage = disk_info.percent
    if disk_usage > DISK_THRESHOLD:
        logging.warning(f"High Disk usage detected: {disk_usage}%")
    return disk_usage

def check_running_processes():
    process_count = len(psutil.pids())
    if process_count > PROCESS_COUNT_THRESHOLD:
        logging.warning(f"High number of running processes detected: {process_count}")
    return process_count

def main():
    logging.info("Starting system health monitoring")
    while True:
        cpu_usage = check_cpu_usage()
        memory_usage = check_memory_usage()
        disk_usage = check_disk_usage()
        process_count = check_running_processes()
        
        # Print current metrics to the console (optional)
        print(f"CPU Usage: {cpu_usage}%")
        print(f"Memory Usage: {memory_usage}%")
        print(f"Disk Usage: {disk_usage}%")
        print(f"Running Processes: {process_count}")
        
        # Sleep for a specified interval before the next check
        time.sleep(60)  # Check every minute

if __name__ == "__main__":
    main()
