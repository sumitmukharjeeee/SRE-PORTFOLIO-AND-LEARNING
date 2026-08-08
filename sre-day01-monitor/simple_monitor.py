import psutil

# 1. Grab current CPU and Memory percentages
cpu_usage = psutil.cpu_percent(interval=1)
memory_usage = psutil.virtual_memory().percent

# 2. Print what we found
print(f"Current CPU Usage: {cpu_usage}%")
print(f"Current Memory Usage: {memory_usage}%")

# 3. Simple threshold logic
if cpu_usage > 80:
    print("ALERT: CPU usage is critically high!")
elif memory_usage > 85:
    print("ALERT: Memory usage is critically high!")
else:
    print("STATUS: Everything is running smoothly.")
