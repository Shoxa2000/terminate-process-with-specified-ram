import psutil
import os

def get_process_memory_usage(pid):
    try:
        process = psutil.Process(pid)
        return process.memory_info().rss / 1024 / 1024  # memory usage in MB
    except psutil.NoSuchProcess:
        return None

def main():
    pid = int(input("Enter the process ID to monitor: "))
    i = 0 # modification to not fall into infinite loop
    while i<10:
        memory_usage = get_process_memory_usage(pid)
        if memory_usage is not None:
            print("Current memory usage of process", pid, ":", memory_usage, "MB")
            exceed_memory = int(input("Enter the maximum RAM to terminate the program: "))
            if memory_usage > exceed_memory:
                print("Memory usage exceeds the specified RAM consumption. Terminating process", pid, "...")
                os.kill(pid, 9)
                break
        else:
            print("Process with ID", pid, "not found.")
            break
        i+=1
if __name__ == "__main__":
    main()