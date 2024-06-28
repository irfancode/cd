import psutil
import platform
import os
import datetime

def get_system_info():
    # Get operating system information
    os_name = platform.system()
    os_version = platform.release()
    
    # Get CPU information
    cpu_count = psutil.cpu_count()
    cpu_freq = psutil.cpu_freq()
    cpu_load = psutil.cpu_percent(interval=1)
    
    # Get memory information
    mem = psutil.virtual_memory()
    total_memory = mem.total / (1024.0 ** 2)
    available_memory = mem.available / (1024.0 ** 2)
    used_memory = mem.used / (1024.0 ** 2)
    memory_percent = mem.percent
    
    # Get disk information
    disk_usage = psutil.disk_usage('/')
    total_disk = disk_usage.total / (1024.0 ** 3)
    used_disk = disk_usage.used / (1024.0 ** 3)
    free_disk = disk_usage.free / (1024.0 ** 3)
    disk_percent = disk_usage.percent
    
    # Get network information
    net_io_counters = psutil.net_io_counters()
    bytes_sent = net_io_counters.bytes_sent
    bytes_recv = net_io_counters.bytes_recv
    
    # Get boot time
    boot_time = datetime.datetime.fromtimestamp(psutil.boot_time()).strftime("%Y-%m-%d %H:%M:%S")
    
    # Print system information
    print(f"Operating System: {os_name} {os_version}")
    print(f"CPU: {cpu_count} cores, {cpu_freq.current:.2f}MHz, {cpu_load:.2f}% utilization")
    print(f"Memory: {total_memory:.2f}GB total, {available_memory:.2f}GB available, {used_memory:.2f}GB used ({memory_percent:.2f}%)")
    print(f"Disk: {total_disk:.2f}GB total, {used_disk:.2f}GB used, {free_disk:.2f}GB free ({disk_percent:.2f}%)")
    print(f"Network: {bytes_sent / (1024.0 ** 2):.2f}MB sent, {bytes_recv / (1024.0 ** 2):.2f}MB received")
    print(f"Boot Time: {boot_time}")

if __name__ == "__main__":
    get_system_info()