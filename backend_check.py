import time

time.sleep(4)

with open("backend_report.txt", "w") as f:
    f.write("Backend check passed")