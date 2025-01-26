import subprocess
import signal
import sys

# Start both scripts
processes = [
    subprocess.Popen(["python3", "interface.py"]),
    subprocess.Popen(["python3", "sim.py"]),
]


def terminate_processes(signal_received, frame):
    print("\nTerminating both scripts...")
    for process in processes:
        process.terminate()
    sys.exit(0)


# Handle CTRL+C
signal.signal(signal.SIGINT, terminate_processes)

# Wait for both scripts
for process in processes:
    process.wait()
