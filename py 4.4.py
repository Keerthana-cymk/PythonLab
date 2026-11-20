
import json

# Create sample log data
logs = [
    {"level": "INFO", "message": "Application started"},
    {"level": "WARNING", "message": "Low memory"},
    {"level": "ERROR", "message": "File not found"},
    {"level": "INFO", "message": "User logged in"},
    {"level": "ERROR", "message": "Connection failed"}
]

# Write logs into JSON file
with open("logs.json", "w") as file:
    json.dump(logs, file, indent=4)

# Read logs from JSON file
with open("logs.json", "r") as file:
    data = json.load(file)

# Analyze logs
info = 0
warning = 0
error = 0

print("--- Log File Contents ---")

for log in data:
    print(log["level"], ":", log["message"])

    if log["level"] == "INFO":
        info += 1
    elif log["level"] == "WARNING":
        warning += 1
    elif log["level"] == "ERROR":
        error += 1

# Display summary
print("\n--- Log Analysis Report ---")
print("Total Logs:", len(data))
print("INFO Messages:", info)
print("WARNING Messages:", warning)
print("ERROR Messages:", error)
