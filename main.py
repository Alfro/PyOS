# PyOS
# Made for Python 2.7.12
# main.py

# Import Libraries

import os
# PyOS Scripts
from internal import extra
from internal import runCommand

# Command Loop

def cmd_loop():
    command = raw_input("> ").lower()
    runCommand.isValid(command)
    cmd_loop()
    
# Initial Code

# Clear the screen
os.system('clear')
# Print the name and version
print(extra.colors.BOLD + extra.os.name + " " + extra.os.ver + extra.colors.ENDC)

print(extra.colors.WARNING + extra.colors.BOLD + "Note: PyOS was designed for Python v2, not v3." + extra.colors.ENDC)
print(extra.os.helpmsg)
cmd_loop()