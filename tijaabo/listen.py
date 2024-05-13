import subprocess

command = "bench start"  # Replace with the desired command you want to execute

# Execute the command
process = subprocess.Popen(command.split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE)

# Wait for the process to finish and capture the output
stdout, stderr = process.communicate()

# Print the output
print("Standard Output:")
print(stdout.decode())

print("Standard Error:")
print(stderr.decode())