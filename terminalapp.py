print("I like climbing ")

import os

print("I like climbing mountains.")

os.system('clear')

# Greeter is a terminal application that greets old friends warmly,
# and remembers new friends.
# Display a title bar.
print("\t**********************************************")
print("\t*** Greeter - Hello old and new friends! ***")
print("\t**********************************************")

# Greeter is a terminal application that greets old friends warmly,
# and remembers new friends.
# Display a title bar.
print("\t**********************************************")
print("\t*** Greeter - Hello old and new friends! ***")
print("\t**********************************************")
# Display a bunch of output, representing a long-running program.
for x in range(0,51):
    print("\nWe have done %d fun and interesting things together!" % x)

# Import the sleep function.
from time import sleep
print("I'm going to sleep now.")
# Sleep for 3 seconds.
sleep(3)
print("I woke up!")


import os
# Greeter is a terminal application that greets old friends warmly,
# and remembers new friends.
# Display a title bar.
print("\t**********************************************")
print("\t*** Greeter - Hello old and new friends! ***")
print("\t**********************************************")
# Print a bunch of information, in short intervals
names = ['aaron', 'brenda', 'cyrene', 'david', 'eric']
# Print each name 5 times.
for name in names:
    # Clear the screen before listing names.
    os.system('clear')
    # Display the title bar.
    print("\t**********************************************")
    print("\t*** Greeter - Hello old and new friends! ***")
    print("\t**********************************************")
    print("\n\n")
    for x in range(0,5):
        print(name.title())
    # Pause for 1 second between batches.
    sleep(1)

from time import sleep
import os
# Greeter is a terminal application that greets old friends warmly,
# and remembers new friends.
def display_title_bar():

    os.system('clear')
    print("\t**********************************************")
    print("\t*** Greeter - Hello old and new friends! ***")
    print("\t**********************************************")

# Print a bunch of information, in short intervals
names = ['aaron', 'brenda', 'cyrene', 'david', 'eric']
# Print each name 5 times.
for name in names:
    display_title_bar()
    print("\n\n")
    for x in range(0,5):
        print(name.title())

sleep(1)


