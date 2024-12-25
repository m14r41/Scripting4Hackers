import multiprocessing
import os
import psutil
import random
import time

def consume_memory(percentage):
    """Consumes the specified percentage of available RAM."""
    available_memory = psutil.virtual_memory().available
    target_memory = int(available_memory * (percentage / 100))
    large_list = []
    allocated_memory = 0

    print(f"Targeting ~{percentage}% of available RAM ({target_memory // (1024 * 1024)} MB)...")
    try:
        while allocated_memory < target_memory:
            large_list.extend([random.random()] * (10 * 1024 * 1024 // 8))  # Allocate 10 MB chunks
            allocated_memory += 10 * 1024 * 1024
            print(f"Allocated: {allocated_memory // (1024 * 1024)} MB", end="\r")
    except MemoryError:
        print("\nMemoryError: Could not allocate further memory.")

    print(f"\nMemory allocation completed at ~{percentage}%.")
    return large_list

def consume_cpu():
    """Consumes CPU by performing endless calculations."""
    print("Worker process consuming CPU...")
    while True:
        _ = sum(i * i for i in range(10000))  # Intensive computation

def monitor_resources():
    """Monitors memory and CPU usage."""
    while True:
        cpu_usage = psutil.cpu_percent(interval=1)
        memory_usage = psutil.virtual_memory().percent
        print(f"CPU Usage: {cpu_usage}% | Memory Usage: {memory_usage}%")
        time.sleep(1)

def main():
    memory_target_percentage = 70
    cpu_target_percentage = 80

    print("Starting resource consumption...")

    # Start memory consumption
    large_list = consume_memory(memory_target_percentage)

    # Start CPU consumption
    num_cores = os.cpu_count()
    num_workers = int(num_cores * (cpu_target_percentage / 100))
    print(f"Starting {num_workers} worker processes to consume ~{cpu_target_percentage}% CPU...")

    processes = [multiprocessing.Process(target=consume_cpu) for _ in range(num_workers)]
    for p in processes:
        p.start()

    # Monitor resource usage
    try:
        monitor_resources()
    except KeyboardInterrupt:
        print("\nTerminating all processes...")

    # Cleanup
    for p in processes:
        p.terminate()
        p.join()
    del large_list
    print("Resources released.")

if __name__ == "__main__":
    main()
