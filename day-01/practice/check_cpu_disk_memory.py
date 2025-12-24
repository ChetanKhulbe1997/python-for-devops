import psutil

def check_cpu_disk_memory():
    cpu_threshold = int(input("Enter the CPU Threshold: "))
    disk_threshold = int(input("Enter the Disk Usage Threshold: "))
    memory_threshold = int(input("Enter the Memory Usage Threshold: "))

    current_cpu = psutil.cpu_percent(interval=1)
    current_disk = psutil.disk_usage('/').percent
    current_memory = psutil.virtual_memory().percent

    print(f"Current CPU Usage: {current_cpu}%")
    print(f"Current Disk Usage: {current_disk}%")
    print(f"Current Memory Usage: {current_memory}%")

    print(f"CPU Threshold Set: {cpu_threshold}%")
    print(f"Disk Threshold Set: {disk_threshold}%")
    print(f"Memory Threshold Set: {memory_threshold}%")

    if current_cpu > cpu_threshold:
        print("CPU Alert Email Sent...")
    else:
        print("CPU is in Safe state")

    if current_disk > disk_threshold:
        print("Disk Alert Email Sent...")
    else:
        print("Disk is in Safe state")

    if current_memory > memory_threshold:
        print("Memory Alert Email Sent...")
    else:
        print("Memory is in Safe state")

check_cpu_disk_memory()