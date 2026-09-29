# Failed Login Analyzer

This script reads a login log and flags accounts with too many failed attempts in a short time frame — a pattern commonly associated with brute-force login attacks.

## How it works
The script reads a log of login attempts line by line. Next it groups failed logins per user with their timestamps. Then flags anyone whose failures hit a threshold within a short time window.

## How to run it
python failed_login_analyzer.py

## What I learned
This project taught me basic principles in Python and how to possibly flag bruteforce attacks. I learned how to create loops, strip certain characters from logs, convert the timestamps into readable data. After completing this project I feel much more comfortable trying my hand at different Python projects and just seeing what else I can create.