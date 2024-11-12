game_active = True

while game_active:
    # Run the game.
    # At some point, the game ends and game_active will be set to False.
    # When that happens, the loop will stop executing.

power = '5'
# The player is allowed to keep playing as long as their power is over 0.
while power > 0:
    print("You are still playing, because your power is %d." % power)
    # Your game code would go here, which includes challenges that make it #
    # possible to lose power.
    # We can represent that by just taking away from the power.
    power = power - 1

print("\nOh no, your power dropped to 0! Game Over.")

variable = input '5'(Please enter a value: '5')