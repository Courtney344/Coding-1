print("I like climbing mountains.")

import os
print("I like climbing mountains")

# clear the screen
os.system('clear')

# Greeter is a terminal application that greets old friends warmly,
# and remembers new friends.

print("\t**********************************************")
print("\t*** Greeter - Hello old and new friends! ***")
print("\t**********************************************")

#Display a bunch of output, representing a long-running program.
for x in range(0,51):
    print("\nWe have done %d fun and interesting things together!" % x)

from time import sleep
print("I'm going to sleep now.")
#Sleep for 3 seconds.
sleep(3)
print("I woke up!")

# Display a title bar.
print("\t**********************************************")
print("\t*** Greeter - Hello old and new friends! ***")
print("\t**********************************************")

names = ['aaron', 'brenda', 'cyrene', 'david', 'eric']
# Print each name 5 times.
for name in names:
    # Pause for 1 second between batches, and then skip two lines.
    sleep(1)
    print("\n\n")
for x in range(0,5):
    print(name.title())

from time import sleep
import os
# Greeter is a terminal application that greets old friends warmly,
#   and remembers new friends.

### FUNCTIONS ###
def display_title_bar():
    # Clears the terminal screen, and displays a title bar.
    os.system('clear')
    print("\t**********************************************")
    print("\t*** Greeter - Hello old and new friends! ***")
    print("\t**********************************************")

### MAIN PROGRAM ###
# Print a bunch of information, in short intervals
names = ['aaron', 'brenda', 'cyrene', 'david', 'eric']
# Print each name 5 times.
for name in names:
    display_title_bar()
    print("\n\n")
    for x in range(0,5):
        print(name.title())
    # Pause for 1 second between batches.
    sleep(1)

def display_title_bar():
    # Clears the terminal screen, and displays a title bar.
    os.system('clear')

display_title_bar()
while choice != 'q':
    display_title_bar()
    # Let users know what they can do.
    print("\n[1] See a list of friends.")
    print("[2] Tell me about someone new.") 
    print("[q] Quit.")
    choice = input("What would you like to do? ")
    # Respond to the user's choice.
    display_title_bar()
    if choice == '1':
    print("\nHere are the people I know.\n") 
    elif choice == '2':
        print("\nI can't wait to meet this person!\n")
    elif choice == 'q':
        print("\nThanks for playing. Bye.")
    else:
        print("\nI didn't understand that choice.\n")
def gauss(numbers):
    for number in numbers:
        while len(numbers)> 0:
            num1 = numbers.pop(0)
            print(num1)
            num2 = numbers.pop(-1)
            print(num2)
            calc = num1 + num2
            print(str(num1)) + "+" + str(num2) + "=" + str(calc)
        print("Final answer is: " + str(num1 * calc))
    
    gauss(list(range(1,101)))