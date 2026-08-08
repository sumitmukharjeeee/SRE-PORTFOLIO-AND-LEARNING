
# 📍 Day 1: Linux System Diagnostics & Python Health Monitor

## 🎯 Objectives
- Set up a lightweight, responsive Linux execution environment using Ubuntu on WSL2.
- Master essential terminal commands for inspecting active processes, memory, and network sockets.
- Build a zero-bloat Python monitoring script (`simple_monitor.py`) to check system resource usage.

---

## 🛠️ Linux Commands Learned & Executed

| Command | Purpose / Usage |
| :--- | :--- |
| `free -h` | Displays total, used, and available system RAM in human-readable format (MB/GB). |
| `ps aux \| grep python` | Lists all active system processes filtered specifically for running Python tasks. |
| `top` | Interactive live task manager showing CPU and Memory usage per process. |
| `ss -tulpn` | Lists all open network listening sockets, active ports, and owning process IDs. |

---

## 🐍 Project 0.1: `simple_monitor.py`

A lightweight Python script using the `psutil` library to collect live hardware telemetry and issue basic status alerts.

### Script Highlights
- Reads real-time CPU percentage over a 1-second sample interval.
- Reads total virtual memory usage percentage.
- Uses threshold logic to flag `CRITICAL` or `HEALTHY` system states.

### How to Run

1. **Install Dependencies:**
   ```bash
   pip install psutil
