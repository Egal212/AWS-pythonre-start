import os

os.system("ls")

import subprocess 
subprocess.run("ls")

subprocess.run(["ls","-l"])
subprocess.run

command="uname"
commandArgument="-a"
print(f'Gathering system information with command: {command} {commandArgument}')
subprocess.run([command,commandArgument])