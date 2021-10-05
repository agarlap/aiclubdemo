
import random

position = 0

for turn in range(1, 6):
    print("Turn #", turn,":")
    dice1 = random.randrange(1, 7)
    print("Dice rolled: ", dice1)
    position = position + dice1
    print("Position: ", position)

print("OVERALL POSITION: ", position)