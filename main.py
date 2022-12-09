import random

# TODO: Add loop + hotkeys to make into functional game
# TODO: Add checkers and point values for different dice groupings
# TODO: Add graphics of some sort


# Generates 5 dice rolls
def rollAllDice():
    dice = [random.randint(1, 6) for x in range(5)]
    return dice


# Keeps specified dice rolls and generates new values for all others
def rollDice(dice, keep):
    for i in range(len(dice)):
        if i not in keep:
            dice[i] = random.randint(1, 6)
    return dice


dice = rollAllDice()
print(dice)
dice = rollDice(dice, [1, 3])
print(dice)
