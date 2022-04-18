# Guessing the number

import random

class GuessNumber:
    def __init__(self):
        self.random_value = 0
        self.min_value = 1
        self.max_value = 100
        self.try_again = True

    def Start(self):
        self.RandomNumberGenerator()
        self.AskRandomNumber()
        while self.try_again is True:
            if int(self.guess_value) > self.random_value:
                print('lower')
                self.AskRandomNumber()
            elif int(self.guess_value) < self.random_value:
                print('higher')
                self.AskRandomNumber()
            else:
                print('CONGRATULATIONS!')
                self.try_again = False

    def AskRandomNumber(self):
        self.guess_value = input('Guess a number: ')

    def RandomNumberGenerator(self):
        self.random_value = random.randint(self.min_value, self.max_value)


guess = GuessNumber()

guess.Start()