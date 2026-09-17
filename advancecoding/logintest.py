
# login automation test framework
# write a python code for login testing framework
#creates folders using pathlib
#1)read credentials from the external file-users.txt, and
#2)create a reusable login function,
#3)executes login test.
#4) determine pass or fail, and 
#5)generate a fresh report/ and
#6)append every execution to logs. with date time, and 

from pathlib import Path                
from datetime import datetime


# Create folders
Path("data").mkdir(exist_ok=True)
Path("logs").mkdir(exist_ok=True)
Path("reports").mkdir(exist_ok=True)


# reusingLogin function
from loginfunc import login
result = login("admin", "password123")
print(result)

# Start execution log
with open("advancecoding/logs/execution.log", "a") as log:
    log.write(f"{datetime.now()} - Test execution started\n")


# Create report
with open("advancecoding/reports/test_report.txt", "w") as report:
    report.write("LOGIN AUTOMATION REPORT\n")
    

# Read login test data 
with open("advancecoding/data/users.txt", "r") as file:

    for line in file:

        username, password = line.strip().split(",")

        # Executing  logintest
        result = login(username, password)

        if result:
            status = "PASS"
        else:
            status = "FAIL"

        print(username, status)

        # append execution-Add result to report
        with open("advancecoding/reports/test_report.txt", "a") as report:
            report.write(f"{username} : {status}\n")


# End execution log
with open("advancecoding/logs/execution.log", "a") as log:
    log.write(f"{datetime.now()} - Test execution completed\n")