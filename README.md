# Failed Login Analyzer

This Python script reads an authentication log and flags users with multiple failed login attempts within a short time window. This is a pattern that can sometimes be associated with brute-force login attacks.

## What This Project Does

I created this project to practice using Python for a cybersecurity-related problem.

The script reads a login log line by line, looks for failed login attempts, and keeps track of those attempts for each user. It then checks if a user has reached a certain number of failed attempts within a specific amount of time.

For this project, the detection rules are:

* **5 or more failed login attempts**
* **Within 15 minutes**

If both conditions are met, the user is flagged.

> A high number of failed login attempts does not automatically mean an attack. This project is a simple example of how login activity could be monitored for potentially suspicious behavior.

## How It Works

The log file is formatted like this:

```text
Timestamp | Username | Source IP | Status
```

The script:

1. Opens the `sample_auth.log` file.
2. Reads each line of the log.
3. Splits the information into the timestamp, username, source IP, and login status.
4. Converts the timestamp into a format Python can work with.
5. Stores failed login times for each user.
6. Checks the number of failures and the amount of time between the first and last attempt.
7. Flags the user if they meet both detection rules.

The main detection logic is:

```text
5+ failed attempts
AND
15 minutes or less between the attempts
```

## Technologies Used

* Python
* `datetime`
* `timedelta`

## Python Concepts I Used

* Reading files
* Loops
* If statements
* Lists
* Dictionaries
* String manipulation
* Splitting log data
* Working with timestamps
* Calculating time differences

## Cybersecurity Concepts

* Authentication logs
* Failed login monitoring
* Brute-force attack detection
* Security thresholds
* Time-based detection
* Suspicious login activity

## How to Run It

Make sure Python is installed and that `sample_auth.log` is in the same folder as the Python script.

Run:

```bash
python failed_login_analyzer.py
```

## Example Log

Here is an example of what the log file can look like:

```text
2026-09-01 10:01:15|alice|192.168.1.10|FAILURE
2026-09-01 10:03:22|alice|192.168.1.10|FAILURE
2026-09-01 10:05:41|alice|192.168.1.10|FAILURE
2026-09-01 10:07:18|alice|192.168.1.10|FAILURE
2026-09-01 10:09:32|alice|192.168.1.10|FAILURE
```

Since there are 5 failed login attempts within 15 minutes, the user would be flagged.

## Example Output

```text
FLAGGED: alice 5 failures in 0:08:17
```

### Failed Login Output (Screenshot)

<p align="center">
  <img width="900" alt="Failed Login Analyzer output" src="https://github.com/user-attachments/assets/a7c690b5-1f8c-467f-b07d-4f5c81c4d927" />
</p>

```

## What I Learned

This project taught me basic principles in Python and how Python can be used to help flag potential brute-force attacks.

I learned how to create loops, strip and split information from logs, store information using dictionaries and lists, and convert timestamps into data that Python can use to calculate the time between login attempts.

I also learned how to create a basic detection rule using a threshold and a time window.

After completing this project, I feel much more comfortable trying my hand at different Python projects and just seeing what else I can create. I'm especially interested in continuing to build projects that combine Python with cybersecurity.

## Future Improvements

There are a few things I would like to improve if I continue working on this project:

* Use the source IP address when analyzing failed login attempts
* Make the threshold and time window configurable
* Generate a report of flagged users
* Export results to CSV or JSON
* Add automated tests
* Improve the detection method to check rolling time windows
* Look for suspicious login attempts across multiple accounts from the same IP

## Limitations

This is a basic project for learning and is not meant to replace a real security monitoring system.

The current version uses a fixed threshold of 5 failed attempts and a 15-minute time window. It groups failed attempts by username and does not currently use the source IP address in the final detection.

## Project Goal

My goal with this project was to get more comfortable with Python while working on something related to cybersecurity.

I wanted to take a basic security problem—repeated failed login attempts—and see if I could write a program that could recognize that pattern in a log.

This project gave me more confidence working with Python and made me want to keep experimenting with different cybersecurity projects.
