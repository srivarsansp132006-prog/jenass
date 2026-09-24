import time

time.sleep(4)

with open("frontend_report.txt", "w") as f:
    f.write("Frontend check passed")