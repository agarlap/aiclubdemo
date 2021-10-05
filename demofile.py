
import random

position = 0

for turn in range(1, 11):
    print("Turn #", turn,":")
    dice1 = random.randrange(1, 7)
    print("Dice 1 rolled: ", dice1)
    dice2 = random.randrange(1, 7)
    print("Dice 2 rolled: ", dice2)
    if (dice1 == dice2):
        print("DOUBLES!")
        dice3 = random.randrange(1, 7)
        print("Dice 3 rolled: ", dice3)
        position = position + dice1 + dice2 + dice3
    else:
        position = position + dice1 + dice2
    print("Position: ", position)

print("OVERALL POSITION: ", position)