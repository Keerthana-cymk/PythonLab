import io 
# Sample log data 
data = """10:00 INFO Application started 
10:05 WARNING Low memory 
10:10 ERROR Database connection failed 
10:15 INFO User logged in 
10:20 ERROR File not found 
10:25 INFO Application closed""" 
try: 
# Open log file in read mode 
 try: 
   file = open("log.txt", "r") 
 except (FileNotFoundError, PermissionError): 
   print("Using sample log data...\n") 
   file = io.StringIO(data) 
 # Read and display log contents   error_count = 0 
 print("----- LOG FILE CONTENTS -----") 
 for line in file: 
   print(line.strip()) 
   if "ERROR" in line: 
     error_count += 1 
 file.close() 
 
 # Display total errors 
 print("\nTotal number of ERROR messages:", error_count) 
except Exception as e: 
 print("Error:", e)
