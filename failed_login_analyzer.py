# Failed Login Analyzer
# Reads an auth log and flags users with many failed logins in a short time window.

from datetime import datetime, timedelta

#The "fail_times" stores each user's list of failure times.

fail_times = {}

# The "datetime.strptime" converts the text to be used as data to derive time between each login attempt.
# We have to convert that text because Python can't retrieve the actual times until it's broken down and properly defined.
with open("sample_auth.log") as f:
    for line in f:
        parts = line.strip().split("|")
        timestamp = parts[0]
        t = datetime.strptime(timestamp, "%Y-%m-%d %H:%M:%S")
        user = parts[1]
        source_ip = parts[2]
        status  = parts[3]
# When logging each failure "append(t)" allows the script to attach a failure timestamp to each user's list.   
        if status == "FAILURE":
            if user not in fail_times:
                fail_times[user] = []
            fail_times[user].append(t)
# The THRESHOLD and WINDOW act as our baseline comparison to what the code defines as suspicious.
# In a brute-force attack a threat actor can attempt to log in to your account many times in a span of seconds.
# THRESHOLD defines the amount of login attempts and WINDOW defines the timespan of the attempts until we find it suspicious and flag it.
THRESHOLD = 5
WINDOW = timedelta(minutes=15)
for name, times in fail_times.items():
    span = times[-1] - times[0]
# The deciding factors that flags them is two things: 
# If the difference between the last failed login attempt and the first reaches or is within the "WINDOW".
# If the number of login attempts reaches or exceeded the "THRESHOLD".
# If both factors are true the account gets flagged.
    if len(times) >= THRESHOLD and span <= WINDOW:
        print("FLAGGED:", name, len(times), "failures in", span)
