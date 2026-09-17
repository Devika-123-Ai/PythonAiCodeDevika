#creates folders using pathlib
#reads usernames/passwords from advancecoding/data/users.txt
#uses a reusable login() function
#checks PASS/FAIL
#creates a report
#appends execution start/end times to a log

from pathlib import Path                
from datetime import datetime


# Create folders
Path("data").mkdir(exist_ok=True)
Path("logs").mkdir(exist_ok=True)
Path("reports").mkdir(exist_ok=True)


# Login function
def login(username, password):
    valid_users = {
        "admin": "password123",
        "aitesting": "python123",
        "aisecurity": "sec engg"
    }

    return valid_users.get(username) == password


# Start execution log
with open("advancecoding/logs/execution.log", "a") as log:
    log.write(f"{datetime.now()} - Test execution started\n")


# Create report
with open("reports/test_report.txt", "w") as report:
    report.write("LOGIN AUTOMATION REPORT\n")
    report.write("LOGIN AUTOMATION REPORT\n")


# Read test data and execute test
with open("advancecoding/data/users.txt", "r") as file:

    for line in file:

        username, password = line.strip().split(",")

        # Execution test
        result = login(username, password)

        if result:
            status = "PASS"
        else:
            status = "FAIL"

        print(username, status)

        # Add result to report
        with open("reports/test_report.txt", "a") as report:
            report.write(f"{username} : {status}\n")


# End execution log
with open("logs/execution.log", "a") as log:
    log.write(f"{datetime.now()} - Test execution completed\n")