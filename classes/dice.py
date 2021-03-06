import random

class Dice:
    """Attempt to model rolling dice."""

    def __init__(self, sides=6):
        """Initialize attributes to describe a die."""
        self.sides = sides

    def roll_die(self):
        """Roll the die to generate a random number."""
        for i in range(self.sides):
            print(random.randint(1, self.sides), end=' ')


six = Dice()

six.roll_die()

print('\n')

ten = Dice(10)

ten.roll_die()

print('\n')

twenty = Dice(20)

twenty.roll_die()
