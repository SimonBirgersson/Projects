# Modules and packages
# A module is a piece of software with specific functionality.
# in a ping pong game, one module would handle drawing the game, and one would handle logic.

# Modules have the file extension ".py"

# EXCERCISE sort all commands in package "re" alphabetically
import re
print(sorted(dir(re)))

# Your code goes here
print(sorted(dir(re)))

# Solution
find_members = []
for member in dir(re):
    if "find" in member:
        find_members.append(member)

print(sorted(find_members))
